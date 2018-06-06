# Parsing: Compulsory assignment

Author:

Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

## G<sub>1</sub>: Grammar in CNF
This grammar is contained in the file grammar1.txt
```
S
S -> A B | B C
A -> B C | C B
B -> B A | C A
C -> B B | A C
A -> 'a'
B -> 'b'
C -> 'c'
```

The CYK chart is the table after the final iteration.

The format of parse tree is:
- nodes: (label \$(left right)# )
- leaf: label{word}

#### G<sub>1</sub>: sample sentences
-  S<sub>1</sub>: "a a a a a"
-  S<sub>2</sub>: "a b"
-  S<sub>3</sub>: "b c b a c"

#### S<sub>1</sub>: CYK chart
Table:
```
[[], ['A'], [], [], [], []]
[[], [], ['A'], [], [], []]
[[], [], [], ['A'], [], []]
[[], [], [], [], ['A'], []]
[[], [], [], [], [], ['A']]
[[], [], [], [], [], []]
```

Backtrace table:
```
[{}, "'a'", {}, {}, {}, {}]
[{}, {}, "'a'", {}, {}, {}]
[{}, {}, {}, "'a'", {}, {}]
[{}, {}, {}, {}, "'a'", {}]
[{}, {}, {}, {}, {}, "'a'"]
[{}, {}, {}, {}, {}, {}]

```

#### S<sub>1</sub>: Parse tree
There is no parse tree for this sentence.

#### S<sub>1</sub>: Conclusion
This sentence does not belong to the grammar.


#### S<sub>2</sub>: CYK chart
Table:
```
[[], ['A'], ['S']]
[[], [], ['B']]
[[], [], []]
```


Backtrace table:
```
[{}, "'a'", {'S': [(1, 'A', 'B')]}]
[{}, {}, "'b'"]
[{}, {}, {}]
```

#### S<sub>2</sub>: Parse tree
```
(S $(A{'a'} B{'b'})# )
```

#### S<sub>2</sub>: Conclusion
This sentence belongs to the grammar and is unambiguous.

#### S<sub>3</sub>: CYK chart
Table:
```
[[], ['B'], ['A', 'S'], ['B', 'S'], ['B', 'S', 'B'], ['A', 'S', 'C', 'A', 'S', 'A', 'S']]
[[], [], ['C'], ['A'], ['A'], ['B', 'C', 'C']]
[[], [], [], ['B'], ['B'], ['A', 'S', 'A', 'S']]
[[], [], [], [], ['A'], ['C']]
[[], [], [], [], [], ['C']]
[[], [], [], [], [], []]
```

Backtrace table:
```
[{}, "'b'", {'A': [(1, 'B', 'C')], 'S': [(1, 'B', 'C')]}, {'S': [(2, 'A', 'B')], 'B': [(1, 'B', 'A')]}, {'S': [(2, 'A', 'B')], 'B': [(1, 'B', 'A'), (3, 'B', 'A')]}, {'A': [(1, 'B', 'C'), (3, 'B', 'C'), (4, 'B', 'C')], 'S': [(1, 'B', 'C'), (3, 'B', 'C'), (4, 'B', 'C')], 'C': [(1, 'B', 'B')]}]
[{}, {}, "'c'", {'A': [(2, 'C', 'B')]}, {'A': [(2, 'C', 'B')]}, {'C': [(3, 'A', 'C'), (4, 'A', 'C')], 'B': [(2, 'C', 'A')]}]
[{}, {}, {}, "'b'", {'B': [(3, 'B', 'A')]}, {'A': [(3, 'B', 'C'), (4, 'B', 'C')], 'S': [(3, 'B', 'C'), (4, 'B', 'C')]}]
[{}, {}, {}, {}, "'a'", {'C': [(4, 'A', 'C')]}]
[{}, {}, {}, {}, {}, "'c'"]
[{}, {}, {}, {}, {}, {}]
```

#### S<sub>3</sub>: Parse tree
```
(S $(B{'b'} (C $((A $(C{'c'} B{'b'})# ) (C $(A{'a'} C{'c'})# ))# ))# )

(S $(B{'b'} (C $((A $(C{'c'} (B $(B{'b'} A{'a'})# ))# ) C{'c'})# ))# )

(S $((B $(B{'b'} (A $(C{'c'} B{'b'})# ))# ) (C $(A{'a'} C{'c'})# ))# )

(S $((B $(B{'b'} (A $(C{'c'} (B $(B{'b'} A{'a'})# ))# ))# ) C{'c'})# )

(S $((B $((B $(B{'b'} (A $(C{'c'} B{'b'})# ))# ) A{'a'})# ) C{'c'})# )

```

#### S<sub>3</sub>: Conclusion
This sentence belongs to the grammar but it is ambiguous because it has 4 parse trees.



## G<sub>2</sub>: Grammar not in CNF
This grammar is contained in the grammar2.txt file.
```
S
S -> NP VP
PP -> P NP
PP -> P N
NP -> N
NP -> Det N
NP -> Det Adj N
NP -> Det Adj N PP
VP -> V NP
VP -> VP PP
NP -> NP PP
Det -> 'a'
Det -> 'an'
Det -> 'the'
N -> 'Batman'
N -> 'street'
N -> 'apple'
V -> 'ate'
V -> 'slept'
P -> 'on'
```

#### G<sub>2</sub>: sample sentences
-  S<sub>4</sub>: "Batman slept on the street"
-  S<sub>5</sub>: "Batman ate an apple"
-  S<sub>6</sub>: "Batman ate an apple on the street"

#### Steps taken to convert G<sub>2</sub> to CNF
##### step 0: Grammar represented in a data structure
The grammar is represented as a dictionary of rules, with each rule having an array of the possible productions.
```
{
    'PP': [['P', 'NP'], ['P', 'N']],
    'Det': [["'a'"], ["'an'"], ["'the'"]],
    'N': [["'Batman'"], ["'street'"], ["'apple'"]],
    'VP': [['V', 'NP'], ['VP', 'PP']],
    'P': [["'on'"]],
    'S': [['NP', 'VP']],
    'V': [["'ate'"], ["'slept'"]],
    'NP': [['N'], ['Det', 'N'], ['Det', 'Adj', 'N'], ['Det', 'Adj', 'N', 'PP'], ['NP', 'PP']]
    }
```

##### step 1: Remove start symbol from RHS
If the start symbol is present in the RHS, create a new start symbol ``S<sub>0</sub> -> S``. Since this rule is not applied, the grammar remains the same.

##### step 2: Remove null productions
Remove all the rules which lead to a null terminal symbol. Since this rule is not applied, the grammar remains the same.

##### step 3: Remove unit productions
Remove rules which only have one non-terminal on the RHS, i.e. of the type ``A -> B``. The grammar G<sub>2</sub> after this transformation becomes:
```
{
    'PP': [['P', 'NP'], ['P', 'N']],
    'Det': [["'a'"], ["'an'"], ["'the'"]],
    'N': [["'Batman'"], ["'street'"], ["'apple'"]],
    'VP': [['V', 'NP'], ['VP', 'PP']],
    'P': [["'on'"]],
    'S': [['NP', 'VP']],
    'V': [["'ate'"], ["'slept'"]],
    'NP': [
        ['Det', 'N'],
        ['Det', 'Adj', 'N'],
        ['Det', 'Adj', 'N', 'PP'],
        ['NP', 'PP'],
        ["'Batman'"],
        ["'street'"],
        ["'apple'"],
        ],
    }
```

##### step 4: Remove large rules
Reduce rules which have more than two non-terminals in the RHS into a new rule containing only two non-terminals in RHS, i.e. ``A -> BCD to A -> XD and X -> BC``. The grammar G<sub>2</sub> after this transformation becomes:
```
{
    'PP': [['P', 'NP'], ['P', 'N']],
    'Y': [['Z', 'N']],
    'Det': [["'a'"], ["'an'"], ["'the'"]],
    'N': [["'Batman'"], ["'street'"], ["'apple'"]],
    'VP': [['V', 'NP'], ['VP', 'PP']],
    'P': [["'on'"]],
    'S': [['NP', 'VP']],
    'V': [["'ate'"], ["'slept'"]],
    'NP': [
        ['Det', 'N'],
        ['Z', 'N'],
        ['Y', 'PP'],
        ['NP', 'PP'],
        ["'Batman'"],
        ["'street'"],
        ["'apple'"],
        ],
    'Z': [['Det', 'Adj']],
    }
```

##### step 5: Remove small rules
Reduce the rules having a terminal and a non-terminal together in the RHS into two rules where one rule has two non-terminals and one rule has the non-terminal, i.e. ``A -> aB to A-> XB and X -> a``. Since this rule is not applied, the grammar remains the same.

#### S<sub>4</sub>: CYK chart
Table:
```
[[], ['N', 'NP'], [], [], [], []]
[[], [], ['V'], [], [], []]
[[], [], [], ['P'], [], ['PP']]
[[], [], [], [], ['Det'], ['NP']]
[[], [], [], [], [], ['N', 'NP']]
[[], [], [], [], [], []]
```

Backtrace table:
```
[{}, "'Batman'", {}, {}, {}, {}]
[{}, {}, "'slept'", {}, {}, {}]
[{}, {}, {}, "'on'", {}, {'PP': [(3, 'P', 'NP')]}]
[{}, {}, {}, {}, "'the'", {'NP': [(4, 'Det', 'N')]}]
[{}, {}, {}, {}, {}, "'street'"]
[{}, {}, {}, {}, {}, {}]
```

#### S<sub>4</sub>: Parse tree
There is no parse tree for this sentence.

#### S<sub>4</sub>: Conclusion
This sentence does not belong to the grammar.

#### S<sub>5</sub>: CYK chart
Table:
```
[[], ['N', 'NP'], [], [], ['S']]
[[], [], ['V'], [], ['VP']]
[[], [], [], ['Det'], ['NP']]
[[], [], [], [], ['N', 'NP']]
[[], [], [], [], []]
```

Backtrace table:
```
[{}, "'Batman'", {}, {}, {'S': [(1, 'NP', 'VP')]}]
[{}, {}, "'ate'", {}, {'VP': [(2, 'V', 'NP')]}]
[{}, {}, {}, "'an'", {'NP': [(3, 'Det', 'N')]}]
[{}, {}, {}, {}, "'apple'"]
[{}, {}, {}, {}, {}]
```

#### S<sub>5</sub>: Parse tree
```
(S $(NP{'Batman'} (VP $(V{'ate'} (NP $(Det{'an'} N{'apple'})# ))# ))# )
```

#### S<sub>5</sub>: Conclusion
This sentence belongs to the grammar and is unambiguous.

#### S<sub>6</sub>: CYK chart
Table:
```
[[], ['N', 'NP'], [], [], ['S'], [], [], ['S']]
[[], [], ['V'], [], ['VP'], [], [], ['VP', 'VP']]
[[], [], [], ['Det'], ['NP'], [], [], ['NP']]
[[], [], [], [], ['N', 'NP'], [], [], ['NP']]
[[], [], [], [], [], ['P'], [], ['PP']]
[[], [], [], [], [], [], ['Det'], ['NP']]
[[], [], [], [], [], [], [], ['N', 'NP']]
[[], [], [], [], [], [], [], []]
```

Backtrace table:
```
[{}, "'Batman'", {}, {}, {'S': [(1, 'NP', 'VP')]}, {}, {}, {'S': [(1, 'NP', 'VP')]}]
[{}, {}, "'ate'", {}, {'VP': [(2, 'V', 'NP')]}, {}, {}, {'VP': [(2, 'V', 'NP'), (4, 'VP', 'PP')]}]
[{}, {}, {}, "'an'", {'NP': [(3, 'Det', 'N')]}, {}, {}, {'NP': [(4, 'NP', 'PP')]}]
[{}, {}, {}, {}, "'apple'", {}, {}, {'NP': [(4, 'NP', 'PP')]}]
[{}, {}, {}, {}, {}, "'on'", {}, {'PP': [(5, 'P', 'NP')]}]
[{}, {}, {}, {}, {}, {}, "'the'", {'NP': [(6, 'Det', 'N')]}]
[{}, {}, {}, {}, {}, {}, {}, "'street'"]
[{}, {}, {}, {}, {}, {}, {}, {}]
```

#### S<sub>6</sub>: Parse tree
```
(S $(NP{'Batman'} (VP $(V{'ate'} (NP $((NP $(Det{'an'} N{'apple'})# ) (PP $(P{'on'} (NP $(Det{'the'} N{'street'})# ))# ))# ))# ))# )

(S $(NP{'Batman'} (VP $((VP $(V{'ate'} (NP $(Det{'an'} N{'apple'})# ))# ) (PP $(P{'on'} (NP $(Det{'the'} N{'street'})# ))# ))# ))# )
```

#### S<sub>6</sub>: Conclusion
This sentence belongs to the grammar but it is ambiguous because it has 2 parses.