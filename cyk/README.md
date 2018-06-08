## Programming language
The code is written in Python 2.7.12

## Libraries required
The code does not need any external libraries besides what is already included in the python distribution.

## How to run
Two command line arguments are to be provided:
- The first is the path to a grammar file.
- The second is the input sentence.

A few examples
```
python cyk.py grammar1.txt "a b"

python cyk.py grammar2.txt "Batman ate an apple on the street"
```

If no arguments are given, the code will use a default value.
 

## Description of the code
#### class Grammar
This object stores the grammar information provided as the input. The class properties are defined in the init method. This class has two other primary functions:
- ``convert_to_cnf()``: It converts the object (self) to CNF if it was not already in CNF
- ``read_grammar_file(filename)``: This function reads a given input file and loads the information into the object (self).

#### class CKYParser
The two methods are:
- parse(string): it takes an input string and returns a parse table and a back trace.
- build_tree(back, table, i, j, label): takes the parse table and back trace table from the parse method and recursively builds a parse tree.

#### console output
An appropriate result is printed on the console after each main function gets executed.

#### main method
- The input grammar file is first loaded into an object of type Grammar.
- the Grammar.convert_to_cnf() function then changes this grammar into CNF.
- the grammar object is then used to initialize an object of type Parser.
- the parse method of the parser object is called with the sentence to be parsed provided as the input.
- the parse method returns a table and a backtrace, both of which are then passed to the build_tree method which returns all the possible parse trees.
