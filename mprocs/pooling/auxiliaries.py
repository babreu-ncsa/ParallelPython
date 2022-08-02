###
# File: auxiliaries.py
# Description: Auxiliary functions for pooling.py
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Tuesday, 2nd August 2022, 10:46:01 am
# Last Modified: Tuesday, 2nd August 2022, 10:46:30 am
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
