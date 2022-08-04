###
# File: functions.py
# Description: Definitions of the functions to be calculated in queueing.py
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Wednesday, 3rd August 2022, 9:46:49 am
# Last Modified: Thursday, 4th August 2022, 1:39:21 pm
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

import numpy as np

def get_stats_from_uniform_dist(nDraws, seed):
    """
    Calculates average and standard deviation of nDraws from NumPy's random.rand().

    Arguments:
        - nDraws (int): number of elements to draw
        - seed (int): random number generator's seed

    Returns:
        - results (list): [average, std]
    """
    np.random.seed(seed)
    x = np.random.rand(nDraws)
    return [x.mean(), x.std()]
