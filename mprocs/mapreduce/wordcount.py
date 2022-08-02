###
# File: worldCount.py
# Description: Generates random text and counts the number of times each word appears using MapReduce.
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Tuesday, 14th June 2022, 8:17:38 am
# Last Modified: Tuesday, 2nd August 2022, 1:29:12 pm
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
from time import perf_counter
from mapreduce import MapReduce

def generate_random_text(nwords, seed):
    """
    Creates a dummy text from tastes according to a fixed probability distribution.

    Inputs:
        nwords (int): Number of words to be generated.
        seed (int): The seed for the random number generator.

    Returns:
        A list with the words
    """
    import numpy as np 
    np.random.seed(seed)
    tastes = ["bitter", "sweet", "sour", "salty", "umami"]
    probs = [0.1, 0.1, 0.1, 0.3, 0.4]
    text = []
    for _ in range(nwords):
        taste = np.random.choice(tastes, p=probs)
        text.append(taste)

    return text

def count_words(entry):
    """
    Combine the occurrences of each word in a dictionary and return a dictionary of words and their counts.
    
    Inputs:
        entry (dict): A dictionary item with words as keys and their occurrences as values.
                            The key is the word and the value is a list with occurences.
                            Example: {word1: [1,1,1,1]}

    Returns:
        A tuple with the word and the final count of occurrences.
    """
    word, occurrences = entry
    return (word, sum(occurrences))


if __name__ == "__main__":
    """
    Creates a list of seeds and builds a MapReduce object with the generate_random_text function as a mapper and the count_words function as a reducer.
    """
    import operator
    from itertools import repeat, chain
    from collections import Counter
    import time

    seeds = [1,2,3,4]
    nwords = 100000

    # serial implementation
    print("---- Serial implementation:")
    start = time.perf_counter()
    totalText = []
    for seed in seeds:
        text = generate_random_text(nwords, seed)
        totalText.append(text)
    counts = dict(Counter(chain(*totalText)))
    counts = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
    for word, count in counts:
        print(f"{word}: {count} ({100*count / (nwords*len(seeds))} %)")
    stop = time.perf_counter()
    print(f"Execution time (s): {stop-start}\n\n")

    # parallel implementation
    print("---- Parallel implementation")
    start = time.perf_counter()
    mapArguments = list(zip(repeat(nwords), seeds))
    mapper = MapReduce(generate_random_text, count_words, num_workers=len(seeds))
    word_counts = mapper(mapArguments)
    word_counts = sorted(word_counts, key=operator.itemgetter(1), reverse=True)
    for word, count in word_counts:
        print(f"{word}: {count} ({100*count / (nwords*len(seeds))} %)")
    stop = time.perf_counter()
    print(f"Execution time (s): {stop-start}")
