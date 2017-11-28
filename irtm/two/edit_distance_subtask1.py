# -*- coding: utf-8 -*-
import sys
import logging
import os
# import bisect
# import pandas as pd
from nltk.metrics.distance import edit_distance
# import string
from collections import OrderedDict

logging.basicConfig(format='%(asctime)s [%(levelname)s]\t%(message)s', level=logging.DEBUG)
# define postings list and dictionary variables
dictionary = dict()
posting_list = []
fmap = dict()
eng_dictionary = dict()


def init_eng_dict(english_words):
    global eng_dictionary
    d = open(english_words)
    for line in d.readlines():
        s = line.strip()
        eng_dictionary[s.lower()] = {"size": 0}
    print(len(eng_dictionary))


def init_fmap(tweets):
    global fmap, eng_dictionary
    f = open(tweets)
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
                fmap[token] = {"size": 1, "isCorrect": False}
            else:
                fmap[token]["size"] += 1
    # print len(fmap)


def minEditDistance(s1):
    minimum = 20
    # sys.maxint
    res = ""
    for token in eng_dictionary:
        temp = edit_distance(s1.lower(), token.lower())
        if temp < minimum:
            minimum = temp
            res = token
            break
    return minimum, res


def onlytweet(tweets, english_words):
    # df = pd.read_csv("tweets", sep="\t",names=['A','B','C','D','E'])
    # df = df[['E']]
    # print len(df)
    # df.to_csv("onlytweet")
    global fmap, eng_dictionary
    init_eng_dict(english_words)
    init_fmap(tweets)
    j = 0
    for token in fmap:
        if (j % 10 == 0):
            print(j)
        if token.lower() in eng_dictionary:
            fmap[token]["isCorrect"] = True
        else:
            minimum, res = minEditDistance(token)
            # eng_dictionary[res]["size"] +=fmap[token]['size']
            fmap[token]["correct_term"] = res
            fmap[token]["edit_distance"] = minimum
        j = j + 1
        # print token,fmap[token]

    fmapSorted = OrderedDict(sorted(fmap.iteritems(), key=lambda x: x[1]['size'], reverse=True))
    i = 0
    for token in fmapSorted:
        if (i == 10):
            break
        if fmap[token]["isCorrect"] is False:
            i = i + 1
            print(token, fmap[token])
            break


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
"""
The program takes the input in the format python inverted-index.py <filename>
"""
if __name__ == '__main__':
    if len(sys.argv) > 3:
        logging.error("too many arguments provided")
    elif len(sys.argv) < 3:
        logging.error("too few arguments provided")
    else:
        logging.debug("tweets filename is " + sys.argv[1])
        logging.debug("english-words filename is " + sys.argv[2])
        # check if the file exists at the given path
        if os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]):
            onlytweet(sys.argv[1], sys.argv[2])
        else:
            logging.error("input file is not present")
