###
# File: dispatchprocess.py
# Description: Sample code to dispatch async processes using multiprocessing.
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Wednesday, 15th June 2022, 10:17:34 am
# Last Modified: Tuesday, 2nd August 2022, 10:42:53 am
#  
# Copyright (c) 2022, Bruno R. de Abreu, National Center for Supercomputing Applications.
# All rights reserved.
# License: This program and the accompanying materials are made available to any individual
#          under the citation condition that follows: On the event that the software is
#          used to generate data that is used implicitly or explicitly for research
#          purposes, proper acknowledgment must be provided in the citations section of
#          publications. This includes both the author's name and the National Center
#          for Supercomputing Applications. If you are uncertain about how to do
#          so, please check this page: https://github.com/babreu-ncsa/cite-me.
#          This software cannot be used for commercial purposes in any way whatsoever.
#          Omitting this license when redistributing the code is strongly disencouraged.
#          The software is provided without warranty of any kind. In no event shall the
#          author or copyright holders be liable for any kind of claim in connection to
#          the software and its usage.
###

import distributions as dists
import multiprocessing as mp
import time

if __name__ == "__main__":
    nSamples = 100000000

    # Serial version
    print("Serial version:")
    start = time.perf_counter()
    dists.sampleUniformDistribution(nSamples)
    dists.sampleGaussianDistribution(nSamples)
    dists.sampleGammaDistribution(nSamples)
    end = time.perf_counter()
    print(f"Execution time: {end - start}")

    # Parallel version
    print("\nParallel version:")
    pUnif = mp.Process(target=dists.sampleUniformDistribution, args=(nSamples,))
    pGaus = mp.Process(target=dists.sampleGaussianDistribution, args=(nSamples,))
    pGamm = mp.Process(target=dists.sampleGammaDistribution, args=(nSamples,))
    start = time.perf_counter()
    pUnif.start()
    pGaus.start()
    pGamm.start()
    pUnif.join()
    pGaus.join()
    pGamm.join()
    end = time.perf_counter()
    print(f"Execution time: {end - start}")