###
# File: pooling.py
# Description: Simple example of data parallelism using multiprocessing. 
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Wednesday, 15th June 2022, 9:33:18 am
# Last Modified: Tuesday, 2nd August 2022, 10:48:59 am
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

import multiprocessing as mp
import time
import auxiliaries as aux

if __name__ == "__main__":
    seeds = [1, 2, 3, 4]
    nTrials = 10000000

    # Serial version
    results_serial = []
    start = time.perf_counter()
    for seed in seeds:
        results_serial.append(aux.calculate_pi(seed, nTrials))
    end = time.perf_counter()
    print("Serial version:")
    print(results_serial)
    print(f"in {end - start} seconds")

    # Parallel version
    print("\nParallel version:")
    pool = mp.Pool(processes=4)
    start = time.perf_counter()
    results_parallel = pool.starmap(aux.calculate_pi, zip(seeds, 4*[nTrials]))
    end = time.perf_counter()
    print(results_parallel)
    print(f"in {end - start} seconds")

