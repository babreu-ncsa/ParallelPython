###
# File: dispatchProcess.py
# Description: Sample code to dispatch async processes using multiprocessing.
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Wednesday, 15th June 2022, 10:17:34 am
# Last Modified: Wednesday, 15th June 2022, 10:48:30 am
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

def sampleUniformDistribution(nSamples):
    """
    Sample a uniform distribution, returns a np.array of samples.
    """
    import numpy as np
    x = np.random.uniform(0.0, 1.0, nSamples)
    print(f"Uniform distribution: avg={x.mean()}, std={x.std()}")
    return

def sampleGaussianDistribution(nSamples):
    """
    Sample a normal distribution, returns a np.array of samples.
    """
    import numpy as np
    x = np.random.normal(0.0, 1.0, nSamples)
    print(f"Gaussian distribution: avg={x.mean()}, std={x.std()}")
    return

def sampleGammaDistribution(nSamples):
    """
    Sample a gamma distribution, returns a np.array of samples.
    """
    import numpy as np
    x = np.random.gamma(1.0, 1.0, nSamples)
    print(f"Gamma distribution: avg={x.mean()}, std={x.std()}")
    return



if __name__ == "__main__":
    import multiprocessing as mp
    import time

    nSamples = 100000000

    # Serial version
    print("Serial version:")
    start = time.perf_counter()
    sampleUniformDistribution(nSamples)
    sampleGaussianDistribution(nSamples)
    sampleGammaDistribution(nSamples)
    end = time.perf_counter()
    print(f"Execution time: {end - start}")

    # Parallel version
    print("\nParallel version:")
    pUnif = mp.Process(target=sampleUniformDistribution, args=(nSamples,))
    pGaus = mp.Process(target=sampleGaussianDistribution, args=(nSamples,))
    pGamm = mp.Process(target=sampleGammaDistribution, args=(nSamples,))
    start = time.perf_counter()
    pUnif.start()
    pGaus.start()
    pGamm.start()
    pUnif.join()
    pGaus.join()
    pGamm.join()
    end = time.perf_counter()
    print(f"Execution time: {end - start}")
