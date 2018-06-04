http://courses.washington.edu/ling571/ling571_fall_2010/slides/cky_cnf.pdf

a short description of the modules/functions/classes you implemented;
• the programming language (with the version indicated), in which you coded;
• a list of libraries or dependencies you used (if any);
• instructions on how to run the code including those on how to install the dependencies
(if necessary);
Important: if your code cannot be run properly after following your instructions,
this leads to the overall fail grade automatically

## Programming language
The code is written in Python 2.7.12

## Libraries required
The code does not need any external libraries besides what is already included in the python distribution.

## How to run

## Description of the code
#### class Grammar
This object stores the grammar information provided as the input. The class properties are defined in the init method. This class has two other primary functions:
- ``convert_to_cnf()``: It converts the object (self) to CNF if it was not already in CNF
- ``read_grammar_file(filename)``: This function reads a given input file and loads the information into the object (self).

#### class CKYParser
The two methods are:
- parse(string)
- build_tree(back, table, i, j, label)
