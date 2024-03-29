###
# File: queue.py
# Description: Example of multiprocessing.Queue
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Tuesday, 2nd August 2022, 1:57:55 pm
# Last Modified: Thursday, 4th August 2022, 12:30:10 pm
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

from multiprocessing import Process, freeze_support, Manager
import time
import auxiliaries as aux
import functions

if __name__ == '__main__':
    freeze_support()
    
    start = time.perf_counter()
    # number of processess
    nprocs = 3

    # define the tasks
    tasks = [(functions.get_stats_from_uniform_dist, (2**25, i)) for i in range(50)]

    # use a manager context to share queues between processes
    manager = Manager()
    task_queue = manager.Queue()
    result_queue = manager.Queue()

    # populate task queue
    for task in tasks:
        task_queue.put(task)

    # after all tasks are in the queue, send a message to stop picking...
    for _ in range(nprocs):
        task_queue.put('STOP')

    # start processes (workers)
    procs = []
    for _ in range(nprocs):
        p = Process(target=aux.worker, args=(task_queue, result_queue))
        p.start()
        procs.append(p)

    # wait until workers are done
    for p in procs:
        p.join()

    # print what's in the result queue
    while not result_queue.empty():
        print(result_queue.get())
        
    stop = time.perf_counter()
    print(f"Execution time (s): {stop-start}")
