# Assignment 1
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219


## Task1
### Subtask a
**inverted positional index**

he   -> 1-2-4-5-9

she  -> 2-3-6-7-8

is   -> 1

nice -> 1-3-9

### Subtask b
using $\sqrt{length}$ formula for optimized skipping

$\sqrt{5}$=2 is the skipping step length

rewritting, the inverted index with skip pointers will be:

he   -> 1-2-4-5-9 + 1-4-9

she  -> 2-3-6-7-8 + 2-6-8

is   -> 1

nice -> 1-3-9 + 1-9

#### Example query
For the query "he" AND "nice", the simple inverted index will require 5 steps for the postings list of "he" and 3 steps for the postings list of "nice". With skip pointers, the 4-9 link will be used in the postings list of "he" to avoid going through 5, thus increasing the efficiency.

## Task 2
No because skip pointers are only effective if we are intersecting postings (in AND scenarios) thus making it more efficent. They have no effect on conjunction required in OR queries.

## Task 3
For car, we are going to store the following in B tree where $ is a special symbol :
car\$,
ar\$c,
r\$ca,
\$car

For X*
Y, look up Y$X* query which answers

- c\*r => r\$c\*

The string r\$ca is finally used for answering this query.

## Task 4
For Gates \\2 Microsoft, it is required that if the doc id is same, the difference between position index of Microsoft and Gates should be equal to 2.

The following comparisions are made:

- The pointers for Gates and Microsoft start from the first document in their respective postings list.
- Gates, doc 1 with Microsoft, doc 1 -> doc id is same, move inside position list
- Gates, doc 1, pos 3 with Microsoft, doc 1, pos 1 -> difference is 2, add Doc 1 to result set, move both pointers to next doc as the position list has ended.
- Gates, doc 2 with Microsoft, doc 2 -> doc id is same, move inside position list
- Gates, doc 2, pos 6 with Microsoft, doc 2, pos 1-> Difference not equal to 2, move Microsoft pos pointer forward
- Gates, doc 2, pos 6 with Microsoft, doc 2, pos 21-> Difference not equal to 2, end of list for Gates, move both pointers to next doc
- Gates, doc 3 with Microsoft, doc 3 -> doc id is same, move inside position index
- Gates, doc 3, pos 2 with Microsoft, doc 3, pos 2-> Difference not equal to 2, move Gates pos pointer forward
- Gates, doc 3, pos 17 with Microsoft, doc 3, pos 2-> Difference not equal to 2, end of list for Microsoft, move both pointers forward to next doc
- Gates, doc 4 with Microsoft, doc 5 -> doc id is not same, move Gates to next doc
- End of postings list for Gates -> Exit and return result set

The result is Doc 1 because Gates is in 3rd postion and it is 2 spaces far from Microsoft which is in 1st position.

## Task 5

**Permuterm index**

_Advantages_

- No postfiltering is required as the result is exact.

_Disadvantages_

- Takes lot of space as in wildcard queries as we have to store all combinations of string modification with special symbol in B tree. eg hello ->
hello\$,
ello\$h,
llo\$he,
lo\$hel,
o\$hell,
\$hello

**K gram index**

_Advantages_

- The postings list is smaller because the number k-grams of a given word is less than all the possible permutations of it. The magnitude of difference is more exemplified in case of bigger words (i.e. having more characters).

_Disadvantages_

- Postfiltering is required to eliminate false positives. For example, while quering red* the boolean query $re AND red can also return "repaired" as a false postive.

## Task 6

__Levenshtein distance__


|   |   | F | L | O | U | R |
| --- | --- | --- | --- | --- | --- | ---|
|  | 0 | 1 | 2 | 3 | 4 | 5|
| F | 1 | 0 | 1 | 2 | 3 | 4 |
| L | 2 | 1 | 0 | 1 | 2 | 3|
| O | 3 | 2 | 1 | 0 | 1 | 2|
| W | 4 | 3 | 2 | 1 | 1 | 2|
| E | 5 | 4 | 3 | 2 | 2 | 2|
| R | 6 | 5 | 4 | 3 | 3 | 2 |


The last cell or bottom right cell is the Levenshtein distance ie in this case it is 2.

Explanation : 

| Cost | Operation | Input | Output |
| --- | --- | --- | --- | 
| 0|(copy) |F |F |
| 0|(copy) |L |L |
| 0|(copy) |O |O |
| 1|replace |W |U |
| 2|delete |E | * |
| 2|(copy) |R|R|

On comparing FLOWER and FLOUR,

- since both letters are 'F', we only copy it, cost incurred in this process is 0.
- similarly for 'L' & 'O', cost incurred is 0.
- since input and output letter ie 'W' and 'U', cost incurred for replacing is 1.
- since 'FLOWER' and 'FLOUR' are of different length, so deleting 1 character. Cost incurred is 1.
- since both letters are same ie 'R', cost incurred is 0. 

Hence the total cost is 2.


## Task 7
Querying l\$re will work if we check each term returned from this query against re\*v\*l and only search the inverted index for those terms satisfying re\*v\*l

The problem with this method is that the permuterm index is quite large since it contains all rotations of each term obtained from the intersection performed above.

One way to solve this problem is to reduce the number of terms for which we have to store the permuterm index. This can be done by quering "l\$re AND v" and perform the intersection with the result of this query. The resulting number of terms satisfying re*v*l will be less in this case.


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