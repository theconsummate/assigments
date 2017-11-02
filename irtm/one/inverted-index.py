#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
import os.path
import bisect


logging.basicConfig(format='%(asctime)s [%(levelname)s]\t%(message)s', level=logging.DEBUG)
dictionary = dict()
posting_list = []

def index(filename):
    global dictionary, posting_list
    f = open(filename)    
    for line in f.readlines():
        cols = line.strip().split("\t")
        if len(cols)<5:
            # insufficient columns, skipping this document
            continue
        for token in cols[4].split():
            if token in dictionary:
                dictionary[token]["size"] += 1
                bisect.insort(posting_list[dictionary[token]["posting_list_index"]], cols[1])
            else:
                dictionary[token] = {"size": 1, "posting_list_index": len(posting_list)}
                posting_list.append([])
                posting_list[-1].append(cols[1])
            # dictionary[token].append(cols[1])
    return dictionary, posting_list


def single_query(term):
    if term in dictionary:
        return posting_list[dictionary[term]["posting_list_index"]]
    else:
        return []

def query(term, *args):
    if len(args) == 0:
        return single_query(term)
    l1 = iter(query(term))
    l2 = iter(query(args[0]))
    l = []
    try:
        ll1 = l1.next()
        ll2 = l2.next()
        while True:
            if ll1 == ll2:
                l.append(ll1)
                ll1 = l1.next()
                ll2 = l2.next()
            elif ll1<ll2:
                ll1 = l1.next()
            else:
                ll2 = l2.next()
    except StopIteration as ex:
        return l

if __name__ == '__main__':
    if len(sys.argv) > 2:
        logging.error("too many arguments provided")
    elif len(sys.argv) < 2:
        logging.error("too few arguments provided")
    else:
        logging.debug("input filename is " + sys.argv[1])
        if os.path.isfile(sys.argv[1]):
            index(sys.argv[1])
            print query("stuttgart")
            print query("bahn")
            print query("stuttgart", "bahn")
        else:
            logging.error("input file is not present")