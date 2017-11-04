# assignement 1

## Task1
### Subtask a
**inverted positional index**

he   -> 1-2-4-5-9

she  -> 2-3-6-7-8

is   -> 1

nice -> 1-3-9

### Subtask b
using $\sqrt{length}$ formula for optimized skipping

$\sqrt{5}$=2 is the skipping

rewritting,
skipped inverted index list
he   -> 1-4-9

she  -> 2-6-8

is   -> 1

nice -> 1-9

@dhruv Example pending

## Task 2
Yes, Because skip pointers are used  if we are intersecting postings (in AND scenarios) thus making it more efficent.

## Task 3
@dhruv update the answer
For car, we are going to store the following in B tree where $ is a special symbol :
car$,
ar$c,
r$ca,
$car

For X*Y,
look up

Y$X*
query which answers

c*r

=> r$c*

## Task 4

Doc id : term(occurences list)

Doc 1 : Gates(3) Microsoft(1)

Doc 2 : Gates(6) Microsoft(1,21)

Doc 3 : Gates(2,17) IBM(3) Microsoft(3)

Doc 4 : Gates(1)

Doc 5 : Microsoft(16,22,51)

Doc 7 : IBM(14)

/k means positional comparisons are made for querying.

The result is Doc 1 because Gates is in 3rd postion and it is 2 spaces far from Microsoft which is in 1st position.

## Task 5
Explain more @dhruv

**Permuterm index**
_Advantages_

No postfiltering

_Disadvantages_

Takes lot of space as in wildcard queries, we have to store all combinations of string modification with special symbol in B tree. eg hello ->
hello$,
ello$h,
llo$he,
lo$hel,
o$hell,
$hello

**K gram index**


## Task 6

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

 ## Task 7

 @dhruv answer this