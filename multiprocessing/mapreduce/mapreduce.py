###
# File: MapReduce.py
# Description: Module to build a map-reduce opearation with multiprocessing
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Tuesday, 14th June 2022, 8:15:28 am
# Last Modified: Tuesday, 14th June 2022, 8:16:27 am
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
# This is entirely based from https://pymotw.com/2/multiprocessing/mapreduce.html
import collections
import itertools
import multiprocessing

class MapReduce(object):

    def __init__(self, map_func, reduce_func, num_workers=None):
        """
        map_func
            Function to map inputs, taking as argument one input value
            and returning a tuple with the key and a value to be reduced.

        reduce_func
            Function to reduce the partitioned version into the final output.
            Takes as argument a key as produced by map_func and a list of values associated with that key.

        num_workers
            The number of workers in the multiprocessing pool. Default is the number of CPUs available.
        """
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)

    def partition(self, mapped_values):
        """
        Organize mapped values by key.
        Returns unsorted sequence of tuples with a key and a list of values.
        """
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        """
        Preprocess inputs through map and reduce functions.

        inputs
            Iterable containing input data to be processed.
        
        chunksize
            Portion of the input data to be handed to each worker.
        """
        map_responses = self.pool.map(self.map_func, inputs, chunksize=chunksize)
        partitioned_data = self.partition(itertools.chain(*map_responses))
        reduced_values = self.pool.map(self.reduce_func, partitioned_data)
        return reduced_values