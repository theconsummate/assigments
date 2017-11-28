# -*- coding: utf-8 -*-
import sys
import logging
import os
# import bisect
# import pandas as pd
from nltk.metrics.distance import edit_distance
# import string
from collections import OrderedDict
from multiprocessing import Process
from six.moves import cPickle as pickle
import glob

logging.basicConfig(filename="logs.txt", filemode='a',
                    format='%(asctime)s [%(levelname)s]\t%(message)s', level=logging.DEBUG)
# define postings list and dictionary variables
dictionary = dict()
posting_list = []
fmap = dict()
eng_dictionary = dict()
PICKLE_FOLDER_NAME = "pickle"


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def init_eng_dict(english_words):
    global eng_dictionary
    d = open(english_words)
    for line in d.readlines():
        s = line.strip()
        eng_dictionary[s.lower()] = {"size": 0}
    logging.debug("length of english dict is " + str(len(eng_dictionary)))


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
            # token is already present in dictionary.
            # increase it's frequency by 1 and insert the tweet id in the postings list
            if isEnglish(token) is False:
                continue
            if '@' == token[0]:
                # this token is probably a username, ignore this
                continue
            if token not in fmap:
                fmap[token] = {"size": 1, "isCorrect": False}
            else:
                fmap[token]["size"] += 1
    # print len(fmap)


def minEditDistance(s1, minimum):
    # sys.maxint
    res = ""
    for token in eng_dictionary:
        temp = edit_distance(s1.lower(), token.lower())
        if temp < minimum:
            minimum = temp
            res = token
    return minimum, res


def chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


def process_fmap_subset(subset, eng_dictionary, partition, starting_min_edit_distance):
    localfmap = dict()
    logging.info(str(partition) + " has started")
    j = 0
    # print(subset[0])
    for token in subset:
        word = token[0]
        localfmap[word] = token[1]
        # if (j % 10 == 0):
        #     logging.debug(str(partition) + "" + str(j))
        if word.lower() in eng_dictionary:
            # logging.debug("found in dict " + word.lower())
            # logging.debug(localfmap[word])
            localfmap[word]["isCorrect"] = True
            # logging.debug(localfmap[word])
        else:
            minimum, res = minEditDistance(word, starting_min_edit_distance)
            # eng_dictionary[res]["size"] +=localfmap[token]['size']
            localfmap[word]["correct_term"] = res
            localfmap[word]["edit_distance"] = minimum
        j = j + 1
    pickle.dump(localfmap, open(PICKLE_FOLDER_NAME + "/" + str(partition), 'wb'), pickle.HIGHEST_PROTOCOL)
    logging.info(str(partition) + " has ended")


def onlytweet(tweets, english_words, num_threads, starting_min_edit_distance):
    # df = pd.read_csv("tweets", sep="\t",names=['A','B','C','D','E'])
    # df = df[['E']]
    # print len(df)
    # df.to_csv("onlytweet")
    global fmap, eng_dictionary
    init_eng_dict(english_words)
    init_fmap(tweets)
    logging.debug("length of fmap: " + str(len(fmap)))
    chunk_size = len(fmap) / num_threads
    df_s = chunks(fmap.items(), chunk_size)
    logging.debug("number of chunks: " + str(len(df_s)))
    jobs = []
    for i, s in enumerate(df_s):
        logging.debug("length of partition " + str(i) + " is " + str(len(df_s[i])))
        j = Process(target=process_fmap_subset, args=(df_s[i], eng_dictionary, i, starting_min_edit_distance))
        # print token,fmap[token]
        jobs.append(j)
    for j in jobs:
        j.start()

    for j in jobs:
        j.join()
    # open pickle files and combine dict
    compiledfmap = dict()
    for iis in range(len(df_s)):
        localfmap = pickle.load(open(PICKLE_FOLDER_NAME + "/" + str(iis), 'rb'))
        compiledfmap.update(localfmap)
    # print(df)
    fmap = compiledfmap


def output_top_10():
    global fmap
    fmapSorted = OrderedDict(sorted(fmap.iteritems(), key=lambda x: x[1]['size'], reverse=True))
    # print(fmapSorted)
    i = 0
    for token in fmapSorted:
        if (i == 10):
            break
        if fmap[token]["isCorrect"] is False:
            i = i + 1
            logging.info(token + ", " + str(fmap[token]))


def remove_files_pickle_folder():
    files = glob.glob(PICKLE_FOLDER_NAME + "/*")
    for f in files:
        os.remove(f)


# init_fmap("only")
"""
The program takes the input in the format python edit_distance_subtask1.py <tweets-filename> <english-dict-filename> <num-threads> <STARTING_EDIT_DISTANCE>
"""
if __name__ == '__main__':
    if len(sys.argv) > 5:
        logging.error("too many arguments provided")
    elif len(sys.argv) < 5:
        logging.error("too few arguments provided")
    else:
        logging.debug("tweets filename is " + sys.argv[1])
        logging.debug("english-words filename is " + sys.argv[2])
        # check if the file exists at the given path
        if os.path.isfile(sys.argv[1]) and os.path.isfile(sys.argv[2]):
            if not os.path.exists(PICKLE_FOLDER_NAME):
                os.makedirs(PICKLE_FOLDER_NAME)
            remove_files_pickle_folder()
            onlytweet(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
            output_top_10()
        else:
            logging.error("input file is not present")
