# Assignment 2
Authors:

1. Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

2. Ishan Adhaulia, st159571@stud.uni-stuttgart.de, Matriculation number: 3319219


## Task1
Jaccard index, J(A,B) = $\frac{|A {\cap} B|}{|A {\cup} B|}$

q = algorithm intersection

d1  = the intersection algorithm for two documents is efficient

d2 = intersection of two or more objects is another smaller object

d3 = intersection algorithm

Rewriting in set forms

q = {algorithm , intersection}

$d_1$  = { the , intersection , algorithm , for , two,  documents , is , efficient }

$d_2$ = { intersection , of , two , or , more  , objects , is , another , smaller , object }

$d_3$ = { intersection , algorithm}

Substituting the values in above formula, we get

$J(q,d_1) = \frac{1}{4}$ = 0.25

$J(q,d_2) = \frac{1}{10}$ = 0.1

$J(q,d_3) = 1$

Since Jaccard index measures similarity, $d_3$ is the most relevant to the given query since it has the maximum Jaccard index.

## Task 2
##### Normalized Term Frequency(tf)

- tf(algorithm) in q = 1/2 = 0.5

- tf(algorithm) in d1 = 1/8 = 0.125

- tf(algorithm) in d2 = 0/10 = 0.0

- tf(algorithm) in d3 = 1/2 = 0.5

- tf(intersection) in q = 1/2 = 0.5

- tf(intersection) in d1 = 1/8 = 0.125

- tf(intersection) in d2 = 1/10 = 0.1

- tf(intersection) in d3 = 1/2 = 0.5

##### Inverse Document Frequency (idf)

- idf(algorithm)  = 1 + $log(\frac{3}{2}) \equiv$ 1.18

- idf(intersection) = 1 + $log(\frac{3}{3})$ = 1

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


##### a) Query and Document1

Dot product(Query, Document1)
     = ((0.59) * (0.1475) + (0.5) * (0.125))
     = 0.147025

||Query|| = $\sqrt{(0.59)^2 + (0.5)^2}$ = 0.7734

||Document1|| = $\sqrt{(0.1475)^2 + (0.125)^2)}$ =  0.1933

Cosine Similarity(Query, Document1) = 0.147025 / 0.14949822
                                        = 0.98356

##### b) Query and Document2

Dot product(Query, Document2)
     = ((0.59) * (0.0) + (0.5) * (0.125))
     = 0.0625

||Query|| = $\sqrt{(0.59)^2 + (0.5)2^2}$ = 0.7734

||Document2|| = $\sqrt{(0.0)^2 + (0.1)^2}$ = 0.1

Cosine Similarity(Query, Document2) = 0.0625 / 0.07734
                                    = 0.8082

#### c) Query and Document3

Dot product(Query, Document1)
     = ((0.59) * (0.59) + (0.5) * (0.5))
     = 0.5981

||Query|| = $\sqrt{(0.59)^2 + (0.5)2^2}$

||Document3|| = $\sqrt{(0.59)^2 + (0.5)2^2}$

Cosine Similarity(Query, Document3) = 0.5981 / 0.5981
                                    = 1


##### Most similar document
Since document 3 has the highest cosine similarity, it is the most relevant for the given query.

## Task 3
#### What information does the task description contain that the master gives to a parser?

- Read documents form the given subset of the input corpus one at a time and output (term,docID)-pairs.
- Write these pairs into j term-partitions. The value of j is provided by the master.

#### What information does the parser report back to the master upon completion of the task?

- A set of j term-partitions containing (term,docID)-pairs.

#### What information does the task description contain that the master gives to an inverter?

- Collect all (term,docID) pairs for a one term partition.
- Sort and write all the pairs to postings list.

#### What information does the inverter report back to the master upon completion of the task?

- The subset of the postings list pertaining to the input partition


## Task 4
#### Logarithmic merging
In this method, we maintain series of indexes, each twice as large from the previous one. We start with the $Z_0$ as in the memory and when its size is increased, then we will create $I_0$ and empty the $Z_0$. Always merging is done when both indexes are of same size. As per more and more indexing is being done, index creation and removal is done.

In Logarithmic merging, $Z_0 <=n , I_0 <= n , I_1 <= 2n , I_2 <= 2^2n ... I_T<= 2^kn$. At any time, some of the powers of theses indexes are initialized. 

Overall index construction time is $\Theta(T \log (T/n))$ because each posting is processed only once on each of the $\log (T/n)$ levels. We trade this efficiency gain for a slow down of query processing; we now need to merge results from $\log (T/n)$ indexes as opposed to just two (the main and auxiliary indexes). 

As in the auxiliary index scheme, we still need to merge very large indexes occasionally (which slows down the search system during the merge), but this happens less frequently and the indexes involved in a merge on average are smaller.
We can use distributed compute cluster for creating multiple $Z_0$ ie basic index unit in memory, by this we can harness its computing power.

Advantage is $log{\frac{t}{n}}/N$ where N is size of the cluster, time for processing and creating indexes is reduced. More parallelism achieved.

Disadvantage is having multiple indexes complicates the maintenance of collection-wide statistics.


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
The given $\gamma$ - string: 11110100001111101010111000 can be broken down into the following numbers

- 111101000 -> 11000 -> 24

- 11111010101 -> 110101 -> 53

- 11000 -> 100 -> 4


Postings list will be 24, 77, 81


## Programming Task - Subtask 1

The ideal max size for edit distance must be 5 (atmost) considering the twitter context. Since the allowed limit for a single tweet is 25 characters

In English, a word is made up of 6-8 characters.
$log_{2}{8}$ = 3 edits

If a word is considered of 25 chars
$log_{2}{25} = 4.64 \equiv$ 5 edits

#### Brief overview of implementation
We have used the NLTK (Natural Language Toolkit) implementation of Levenshtein distance in python.

The basic algorithm is as follows:

##### Command line parameters

The program takes the input in the format python edit_distance_subtask1.py \<tweets-filename\> \<english-dict-filename\> \<num-threads\> \<starting_edit_distance\>
- \<tweets-filename\>: path of the tweets file
- \<english-dict-filename\>: path of the tweets file
- \<num-threads\>: number of parallel threads to open
- \<starting_edit_distance\>: the maximum threshold distance under corrections will be considered for an out of dictionary word.

**We executed the code with starting_edit_distance = 5**

##### Preprocessing
- Written in the first few lines of the method `parse_tweets`
- Read the english words dictionary into memory. Case has been ignored.
- Ignore tokens which have characters outside the English letters.
- Ignore tokens starting with "@" as these are probably usernames and there is no need check for spellings.
- Read the tweets into a frequency map. The data structure is a dictionary has the structure -> <key> : {"size": <int>, "isCorrect": <Boolean>}. The "size" field is the frequency of that particular token.

##### spelling correction
- written in the method `process_fmap_subset`
- iterates the given set of tokens and checks if they are correct or not.
- A token is correct it is in the dictionary.
- For other tokens, we find the minimum edit distance from a word in the english dictionary.

##### running parallel threads
- The function `parse_tweets` breaks the input tweets file into `num_threads` partitions and starts a new thread for each partition. The thread executes the `process_fmap_subset` and writes the output for that particular partition (i.e. min edit distance and correct word) into a `pickle` file on the disk.

- After all threads have finished, `parse_tweets` function combines all the partition results into a single dictionary.

#### Code
```python
# -*- coding: utf-8 -*-
import sys
import logging
import os
from nltk.metrics.distance import edit_distance
from collections import OrderedDict
from multiprocessing import Process
from six.moves import cPickle as pickle
import glob

# init logging
logging.basicConfig(filename="logs.txt", filemode='a',
                    format='%(asctime)s [%(levelname)s]\t%(message)s', level=logging.DEBUG)

# define our data structures
dictionary = dict()
posting_list = []
fmap = dict()
eng_dictionary = dict()
PICKLE_FOLDER_NAME = "pickle"


"""
Check if a word belongs in the English charset or not.
"""


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


"""
init the input english dictionary file and load it as global variable
"""


def init_eng_dict(english_words):
    global eng_dictionary
    d = open(english_words)
    for line in d.readlines():
        s = line.strip()
        # ignore case
        eng_dictionary[s.lower()] = {"size": 0}
    logging.debug("length of english dict is " + str(len(eng_dictionary)))


"""
init the input tweets file and load into a frequency map dictionary
"""


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
            # ignore if token has non-english chars
            if isEnglish(token) is False:
                continue
            # ignore twitter usernames
            if '@' == token[0]:
                # this token is probably a username, ignore this
                continue
            # token is already present in dictionary.
            # increase it's frequency by 1
            if token not in fmap:
                fmap[token] = {"size": 1, "isCorrect": False}
            else:
                fmap[token]["size"] += 1
    # print len(fmap)


"""
Calculate the min edit distance for a given word from a word present in our english dictionary
"""


def minEditDistance(s1, minimum):
    # sys.maxint
    res = ""
    for token in eng_dictionary:
        temp = edit_distance(s1.lower(), token.lower())
        if temp < minimum:
            minimum = temp
            res = token
        if minimum == 1:
            break
    return minimum, res


"""
Split the given list into n partitions
"""


def chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


"""
process a given partition and write the correspoding output as a pickle file on the disk
"""


def process_fmap_subset(subset, eng_dictionary, partition, starting_min_edit_distance):
    localfmap = dict()
    logging.info(str(partition) + " has started")
    for token in subset:
        word = token[0]
        localfmap[word] = token[1]
        # word is in the dictionary so it is correct
        if word.lower() in eng_dictionary:
            localfmap[word]["isCorrect"] = True
        else:
            minimum, res = minEditDistance(word, starting_min_edit_distance)
            # eng_dictionary[res]["size"] +=localfmap[token]['size']
            localfmap[word]["correct_term"] = res
            localfmap[word]["edit_distance"] = minimum
    pickle.dump(localfmap, open(PICKLE_FOLDER_NAME + "/" + str(partition), 'wb'), pickle.HIGHEST_PROTOCOL)
    logging.info(str(partition) + " has ended")


def parse_tweets(tweets, english_words, num_threads, starting_min_edit_distance):
    global fmap, eng_dictionary

    init_eng_dict(english_words)
    init_fmap(tweets)

    logging.debug("length of fmap: " + str(len(fmap)))

    # split into multiple threads
    chunk_size = len(fmap) / num_threads
    df_s = chunks(fmap.items(), chunk_size)
    logging.debug("number of chunks: " + str(len(df_s)))
    jobs = []
    for i, s in enumerate(df_s):
        logging.debug("length of partition " + str(i) + " is " + str(len(df_s[i])))
        j = Process(target=process_fmap_subset, args=(df_s[i], eng_dictionary, i, starting_min_edit_distance))
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
            parse_tweets(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
            output_top_10()
        else:
            logging.error("input file is not present")

```