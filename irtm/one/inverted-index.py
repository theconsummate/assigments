#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
import os.path
import bisect


logging.basicConfig(format='%(asctime)s [%(levelname)s]\t%(message)s', level=logging.DEBUG)


def index(filename):
    f = open(filename)
    dictionary = dict()
    posting_list = []
    for line in f.readlines()[:10]:
        cols = line.strip().split("\t")
        for token in cols[4].split():
            if token in dictionary:
                dictionary[token]["size"] += 1
                bisect.insort(posting_list[dictionary[token]["posting_list_index"]], cols[1])
            else:
                dictionary[token] = {"size": 1, "posting_list_index": len(posting_list)}
                posting_list.append([])
                posting_list[-1].append(cols[1])
            # dictionary[token].append(cols[1])
    logging.debug(dictionary['to'])
    logging.debug(posting_list[dictionary['to']["posting_list_index"]])

if __name__ == '__main__':
    if len(sys.argv) > 2:
        logging.error("too many arguments provided")
    elif len(sys.argv) < 2:
        logging.error("too few arguments provided")
    else:
        logging.debug("input filename is " + sys.argv[1])
        if os.path.isfile(sys.argv[1]):
            index(sys.argv[1])
        else:
            logging.error("input file is not present")