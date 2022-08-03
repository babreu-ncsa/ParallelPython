###
# File: auxiliaries.py
# Description: Auxiliaries for queueing.py
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Wednesday, 3rd August 2022, 9:38:42 am
# Last Modified: Wednesday, 3rd August 2022, 12:26:51 pm
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
from multiprocessing import current_process

def calculate(func, args):
    """
    Calculates a certain function for a list of arguments. Returns a string with the result.

    Arguments:
        - func (string): function name
        - args (list): list of arguments
    """
    result = func(*args)
    string = current_process().name
    string = string + " says " + func.__name__ + str(args)
    string = string + " = " + str(result)
    return string


def worker(inputQueue, outputQueue):
    """
    Picks up work from the inputQueue and outputs result to outputQueue.

    Inputs:
        - inputQueue (multiprocessing.Queue)
        - outputQueue (multiprocessing.Queue)
    """
    for func, args in iter(inputQueue.get, 'STOP'):
        result = calculate(func, args)
        outputQueue.put(result)

