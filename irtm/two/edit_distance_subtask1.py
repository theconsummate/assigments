# -*- coding: utf-8 -*-
import sys
import logging
import os.path
import bisect
#import pandas as pd
from nltk.metrics.distance import edit_distance
import string
from collections import OrderedDict

logging.basicConfig(format='%(asctime)s [%(levelname)s]\t%(message)s', level=logging.DEBUG)
# define postings list and dictionary variables
dictionary = dict()
posting_list = []
fmap = dict()
eng_dictionary = dict()

def init_eng_dict(filename2):
    global eng_dictionary
    d = open(filename2)
    for line in d.readlines():
        s = line.strip()
        eng_dictionary[s.lower()] = {"size":0}
    print len(eng_dictionary)

def init_fmap(filename1):
    global fmap, eng_dictionary
    f = open(filename1)
    for line in f.readlines():
        cols = line.strip().split("\t")
        if len(cols) < 5:
            # insufficient columns, skipping this document
            continue
        # col[4] contains the tweet. Tokenise it on whitespaces and add to index
        for token in cols[4].split():
            # toke is already present in dictionary.
            # increase it's frequency by 1 and insert the tweet id in the postings list
            if token not in fmap:
                fmap[token] = {"size" :1 , "isCorrect" : False}
            else :
                fmap[token]["size"] += 1
    #print len(fmap)

def minEditDistance(s1):
    minimum = 20#sys.maxint
    res = ""
    for token in eng_dictionary:
        temp = edit_distance(s1.lower(),token.lower())
        if temp < minimum:
            minimum = temp
            res = token
            break;
    return minimum,res 

def onlytweet(filename1,filename2):
    # df = pd.read_csv("tweets", sep="\t",names=['A','B','C','D','E'])
    # df = df[['E']]
    # print len(df)
    # df.to_csv("onlytweet")
    global fmap, eng_dictionary
    init_eng_dict(filename2)
    init_fmap(filename1)
    j = 0
    for token in fmap:
        if (j%10==0):
            print j
        if token.lower() in eng_dictionary:
            fmap[token]["isCorrect"] = True
        else:
            minimum,res = minEditDistance(token)
            # eng_dictionary[res]["size"] +=fmap[token]['size']
            fmap[token]["correct_term"] = res
            fmap[token]["edit_distance"] = minimum
        j= j+1
        #print token,fmap[token]

    fmapSorted = OrderedDict(sorted(fmap.iteritems(), key=lambda x: x[1]['size'] , reverse=True))
    i = 0
    for token in fmapSorted: 
        if (i==10):
            break
        if fmap[token]["isCorrect"]==False:
            i = i+1
            print token,fmap[token]
            break
        
"""
This file implements an inverted index using a list of tweets as input corpus.
The tweet id is used as a document id in the postings list.
"""

def index(filename):
    """
    implements an inverted index. Takes a valid file path as an input
    Output: None. Initialized the global dictionary and postings_list variables.
    """

    global dictionary, posting_list
    f = open(filename)
    for line in f.readlines():
        cols = line.strip().split("\t")
        if len(cols) < 5:
            # insufficient columns, skipping this document
            continue
        # col[4] contains the tweet. Tokenise it on whitespaces and add to index
        for token in cols[4].split():
            # toke is already present in dictionary.
            # increase it's frequency by 1 and insert the tweet id in the postings list
            if token in dictionary:
                dictionary[token]["size"] += 1
                bisect.insort(posting_list[dictionary[token]["posting_list_index"]],
                              cols[1])

            # new token encountered. Insert it into our data structures
            else:
                dictionary[token] = {"size": 1, "posting_list_index": len(posting_list)}
                posting_list.append([])
                posting_list[-1].append(cols[1])
            # dictionary[token].append(cols[1])
    return dictionary, posting_list


def single_query(term):
    """
    returns the postings list for the query of a single term from the index
    """
    if term in dictionary:
        return posting_list[dictionary[term]["posting_list_index"]]
    else:
        return []


def query(term, *args):
    """
    Method overloading
    calls the single_query method if only one term is provived.
    If two terms are provided via the *args parameter,
    the intersection of the postings list is returned.
    """
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
            elif ll1 < ll2:
                ll1 = l1.next()
            else:
                ll2 = l2.next()
    except StopIteration as ex:
        return l

# init_fmap("only")
onlytweet("tweets","english-words")
# """
# The program takes the input in the format python inverted-index.py <filename>
# """
# if __name__ == '__main__':
#     if len(sys.argv) > 2:
#         logging.error("too many arguments provided")
#     elif len(sys.argv) < 2:
#         logging.error("too few arguments provided")
#     else:
#         logging.debug("input filename is " + sys.argv[1])
#         # check if the file exists at the given path
#         if os.path.isfile(sys.argv[1]):
#             # create index by reading the given tweets file
#             index(sys.argv[1])
#             logging.debug(query("stuttgart"))
#             logging.debug(query("bahn"))
#             logging.debug(query("stuttgart", "bahn"))
#         else:
#             logging.error("input file is not present")
