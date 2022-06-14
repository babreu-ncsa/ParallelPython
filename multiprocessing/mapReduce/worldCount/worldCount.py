###
# File: worldCount.py
# Description: Generates random text and counts the number of times each word appears using MapReduce.
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Tuesday, 14th June 2022, 8:17:38 am
# Last Modified: Tuesday, 14th June 2022, 8:49:16 am
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
from ..MapReduce import MapReduce

def generate_random_text(seed):
    """
    Creates a dummy text from tastes according to a fixed probability distribution.

    Inputs:
        seed (int): The seed for the random number generator.

    Returns:
        A dictionary of words and their occurrences without performing the sum.
    """
    import numpy as np 
    np.random.seed(seed)
    tastes = ["bitter", "sweet", "sour", "salty", "umami"]
    probs = [0.1, 0.1, 0.1, 0.3, 0.4]
    text = []
    for i in range(100):
        taste = np.random.choice(tastes, p=probs)
        text.append((taste, 1))

    return text

def count_words(text_dict):
    """
    Given a dictionary from generate_random_text, combine the occurrences of each word in it and return a dictionary of words and their counts.
    
    Inputs:
        text_dict (dict): A dictionary with words as keys and their occurrences as values.

    Returns:
        A dictionary of words and their final counts.
    """
    word, occurrences = text_dict
    return (word, sum(occurrences))


if __name__ == "__main__":
    """
    Creates a list of seeds and builds a MapReduce object with the generate_random_text function as a mapper and the count_words function as a reducer.
    """
    import operator

    seeds = [1,2,3,4]
    mapper = MapReduce(generate_random_text, count_words, num_workers=4)
    word_counts = mapper(seeds)
    word_counts = sorted(word_counts, key=operator.itemgetter(1), reverse=True)
    for word, count in word_counts:
        print(f"{word}: {count}")

