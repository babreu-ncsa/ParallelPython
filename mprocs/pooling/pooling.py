###
# File: pooling.py
# Description: Simple example of data parallelism using multiprocessing. 
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Wednesday, 15th June 2022, 9:33:18 am
# Last Modified: Wednesday, 15th June 2022, 9:58:32 am
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

def calculate_pi(seed, nTrials=10000):
    """
    Calculate the value of pi using the Monte Carlo method.
    """
    import random
    random.seed(seed)
    inside = 0
    for i in range(nTrials):
        x = random.random()
        y = random.random()
        if (x**2 + y**2 <= 1):
            inside += 1

    return 4.0 * inside / nTrials

if __name__ == "__main__":
    """
    Calculate pi four times using serial and parallel versions.
    """
    import time
    import multiprocessing as mp
    seeds = [1, 2, 3, 4]
    nTrials = 1000

    # Serial version
    results_serial = []
    start = time.perf_counter()
    for seed in seeds:
        results_serial.append(calculate_pi(seed, nTrials))
    end = time.perf_counter()
    print("Serial version:")
    print(results_serial)
    print(f"in {end - start} seconds")

    # Parallel version
    print("\nParallel version:")
    pool = mp.Pool(processes=4)
    start = time.perf_counter()
    results_parallel = pool.starmap(calculate_pi, zip(seeds, 4*[nTrials]))
    end = time.perf_counter()
    print(results_parallel)
    print(f"in {end - start} seconds")

