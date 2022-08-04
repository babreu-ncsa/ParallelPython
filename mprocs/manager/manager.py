###
# File: manager.py
# Description: 
# Author: Bruno R. de Abreu  |  babreu at illinois dot edu
# National Center for Supercomputing Applications (NCSA)
#  
# Creation Date: Wednesday, 3rd August 2022, 1:31:48 pm
# Last Modified: Thursday, 4th August 2022, 3:22:04 pm
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

from multiprocessing import Manager, Process, current_process
import random
import time

class Store:
    def __init__(self):
        # Dictionary with key as the item id and the value as the price
        self.price_book = {}
        # Dictionary with key as the transaction id and the value as the quantity
        self.transaction_book = {}
        # Receipts for each transaction
        self.receipts = []
    
    def create_random_data(self, nItems, nTransactions):
        for i in range(nItems):
            self.price_book[i] = random.randint(1, 1000)
        for i in range(nTransactions):
            items = {}
            for j in range(random.randint(1, 10)):
                items[random.randint(0, nItems - 1)] = random.randint(1, 10)
            self.transaction_book[i] = items

def print_receipt(transaction, price_list):
    string = "Receipt for transaction {}:".format(transaction[0])
    order = transaction[1]
    total = 0
    for item in order.items():
        partial_total = item[1] * price_list[item[0]]
        string += "\n{}: {} x {} each = {}".format(item[0], item[1], price_list[item[0]], partial_total)
        total += partial_total
    string += "\nTotal: {}".format(total)

    return string


if __name__ == "__main__":
    store = Store()
    store.create_random_data(100,100000)

    for transaction in store.transaction_book.items():
        receipt = print_receipt(transaction, store.price_book)
        store.receipts.append(receipt)
    for receipt in store.receipts:
        print(receipt)


    #p1 = Process(target=print_list, args=(l,True, lock))
    #p2 = Process(target=print_list, args=(l,True, lock))
    #p1.start()
    #p2.start()
    #p1.join()
    #p2.join()

