# Assignment 1
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219


## Task1
Jaccard index, J(A,B) = $\frac{A {\bigcap} B}{A {\bigcup} B}$

q = algorithm intersection

d1  = the intersection algorithm for two documents is efficient

d2 = intersection of two or more objects is another smaller object

d3 = intersection algorithm

Rewriting in set forms

q = {algorithm , intersection}

d1  = { the , intersection , algorithm , for , two,  documents , is , efficient }

d2 = { intersection , of , two , or , more  , objects , is , another , smaller , object }

d3 = { intersection , algorithm}
Substituting the values in above formula, we get

J(q,d1) = $\frac{1}{4}$ = 0.25

J(q,d2) = $\frac{1}{10}$ = 0.1

J(q,d3) = $1$

## Task 2
Normalized Term Frequency(tf)

tf (algorithm) in q = 1/2 = 0.5

tf(algorithm) in d1 = 1/8 = 0.125

tf(algorithm) in d2 = 0/10 = 0.0

tf(algorithm) in d3 = 1/2 = 0.5

tf (intersection) in q = 1/2 = 0.5

tf(intersection) in d1 = 1/8 = 0.125

tf(intersection) in d2 = 1/10 = 0.1

tf(intersection) in d3 = 1/2 = 0.5


Inverse Document Frequency (idf)

idf(algorithm)  = 1 + $log(\frac{3}{2}) \equiv$ 1.18

idf(intersection) = 1 + $log(\frac{3}{3})$ = 1

|Document|term|tf|idf|tf*idf|
|---|---|---|---|---|
|q|algorithm|0.5|1.18|0.59|
|d1|algorithm|0.125|1.18|0.1475|
|d2|algorithm|0.0|1.18|0.0|
|d3|algorithm|0.5|1.18|0.59|
|q|intersection|0.5|1.0|0.5|
|d1|intersection|0.125|1.0|0.125|
|d2|intersection|0.1|1.0|0.1|
|d3|intersection|0.5|1.0|0.5|


a) Query and Document1

Dot product(Query, Document1)
     = ((0.59) * (0.1475) + (0.5) * (0.125))
     = 0.147025

||Query|| = $\sqrt{(0.59)^2 + (0.5)^2}$ = 0.7734

||Document1|| = $\sqrt{(0.1475)^2 + (0.125)^2)}$ =  0.1933

Cosine Similarity(Query, Document1) = 0.147025 / 0.14949822
                                        = 0.98356

b) Query and Document2

Dot product(Query, Document2)
     = ((0.59) * (0.0) + (0.5) * (0.125))
     = 0.0625

||Query|| = $\sqrt{(0.59)^2 + (0.5)2^2}$ = 0.7734

||Document2|| = $\sqrt{(0.0)^2 + (0.1)^2}$ = 0.1

Cosine Similarity(Query, Document2) = 0.0625 / 0.07734
                                    = 0.8082

c) Query and Document3

Dot product(Query, Document1)
     = ((0.59) * (0.59) + (0.5) * (0.5))
     = 0.5981

||Query|| = $\sqrt{(0.59)^2 + (0.5)2^2}$

||Document3|| = $\sqrt{(0.59)^2 + (0.5)2^2}$

Cosine Similarity(Query, Document3) = 0.5981 / 0.5981
                                    = 1


## Task 3

## Task 4

## Task 5

### Subtask 5.1
M = K$T^{b}$
Taking $log_{10}$ on both sides of the above equation,

=> $log_{10}K$ + b$log_{10}T$  = $log_{10}M$

Substituting values and solving in the above equation, we get 

a)
M  = $10^5$ 
 
T = $10^7$

$log_{10}(K)$ + 7b = 5

b)
M  = $30000$ 
 
T = $10^6$

$log_{10}(K)$ + 7b = 5

$log_{10}(K)$ + 6b = 4.477121254719662

Solving equation a) and b), we get 
K = 21.8699, b = 0.522879 

### Subtask 5.2
M = K$T^{b}$

Substituting values of K, T and  b in the Eqn
 
 M = 1111111.89571 
 
 => M = 1111112 


## Task 6
Zipf’s law holds exactly for this collection ie (a > b > c > d) 

Assuming the value of 'a' be x then, 

a = $\frac{x}{1}$ , b = $\frac{x}{2}$ , c = $\frac{x}{3}$  , d  = $\frac{x}{4}$

=> $\frac{25x}{12}$=6000

solving for x, x = 2880.

Hence a = 2880, b = 1440, c = 960, d = 720 

## Task 7
 $217_{10}$

In VB code: 0000 0001 1101 1001

In Gamma Code:

Offset = 101 1001

Length $7_{10}$ = $11111110_1$

Gamma code: 11111110 1011001

## Task 8


### Programming Task
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
import os.path
import bisect


logging.basicConfig(format='%(asctime)s [%(levelname)s]\t%(message)s', level=logging.DEBUG)
# define postings list and dictionary variables
dictionary = dict()
posting_list = []


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


"""
The program takes the input in the format python inverted-index.py <filename>
"""
if __name__ == '__main__':
    if len(sys.argv) > 2:
        logging.error("too many arguments provided")
    elif len(sys.argv) < 2:
        logging.error("too few arguments provided")
    else:
        logging.debug("input filename is " + sys.argv[1])
        # check if the file exists at the given path
        if os.path.isfile(sys.argv[1]):
            # create index by reading the given tweets file
            index(sys.argv[1])
            logging.debug(query("stuttgart"))
            logging.debug(query("bahn"))
            logging.debug(query("stuttgart", "bahn"))
        else:
            logging.error("input file is not present")

```