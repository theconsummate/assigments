# Parsing: Compulsory assignment

Author:

Dhruv Mishra, st154709@stud.uni-stuttgart.de, Matriculation number: 3293775

## G<sub>1</sub>: Grammar in CNF
```
```

#### G<sub>1</sub>: sample sentences
-  S<sub>1</sub>:
-  S<sub>2</sub>:
-  S<sub>3</sub>:

#### S<sub>1</sub>: CYK chart
```
```

#### S<sub>1</sub>: Parse tree
```
```

#### S<sub>1</sub>: Conclusion


#### S<sub>2</sub>: CYK chart
```
```

#### S<sub>2</sub>: Parse tree
```
```

#### S<sub>2</sub>: Conclusion


#### S<sub>3</sub>: CYK chart
```
```

#### S<sub>3</sub>: Parse tree
```
```

#### S<sub>3</sub>: Conclusion



## G<sub>2</sub>: Grammar not in CNF
```
```

#### G<sub>2</sub>: sample sentences
-  S<sub>4</sub>:
-  S<sub>5</sub>:
-  S<sub>6</sub>:

#### Steps taken to convert G<sub>2</sub> to CNF
##### step 1: Remove start symbol from RHS
If the start symbol is present in the RHS, create a new start symbol ``S<sub>0</sub> -> S``. The grammar G<sub>2</sub> after this transformation becomes:
```
```

##### step 2: Remove null productions
Remove all the rules which lead to a null terminal symbol. The grammar G<sub>2</sub> after this transformation becomes:
```
```

##### step 3: Remove unit productions
Remove rules which only have one non-terminal on the RHS, i.e. of the type ``A -> B``. The grammar G<sub>2</sub> after this transformation becomes:
```
```

##### step 4: Remove large rules
Reduce rules which have more than two non-terminals in the RHS into a new rule containing only two non-terminals in RHS, i.e. ``A -> BCD to A -> XD and X -> BC``. The grammar G<sub>2</sub> after this transformation becomes:
```
```

##### step 5: Remove small rules
Reduce the rules having a terminal and a non-terminal together in the RHS into two rules where one rule has two non-terminals and one rule has the non-terminal, i.e. ``A -> aB to A-> XB and X -> a``. The grammar G<sub>2</sub> after this transformation becomes:
```
```

#### S<sub>4</sub>: CYK chart
```
```

#### S<sub>4</sub>: Parse tree
```
```

#### S<sub>4</sub>: Conclusion


#### S<sub>5</sub>: CYK chart
```
```

#### S<sub>5</sub>: Parse tree
```
```

#### S<sub>5</sub>: Conclusion


#### S<sub>6</sub>: CYK chart
```
```

#### S<sub>6</sub>: Parse tree
```
```

#### S<sub>6</sub>: Conclusion



## G<sub>2</sub>: Grammar not in CNF
```
```
