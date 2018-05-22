

class Grammar():
    def __init__(self):
        self.variables = list()
        self.terminals = list()
        # this will be a list of lambda functions
        self.productions = list()
        self.start = list()

    def convert_to_cnf(self):
        pass


    def read_grammar_file(self, filename):
        pass

"""
Pseudo code:
https://en.wikipedia.org/wiki/CYK_algorithm
let the input be a string I consisting of n characters: a1 ... an.
let the grammar contain r nonterminal symbols R1 ... Rr, with start symbol R1.
let P[n,n,r] be an array of booleans. Initialize all elements of P to false.
for each s = 1 to n
  for each unit production Rv -> as
    set P[1,s,v] = true
for each l = 2 to n -- Length of span
  for each s = 1 to n-l+1 -- Start of span
    for each p = 1 to l-1 -- Partition of span
      for each production Ra -> Rb Rc
        if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true
if P[n,1,1] is true then
  I is member of language
else
  I is not member of language
"""
class CYKParser():
    """
    constructor for the parser class.
    """
    def __init__(self, grammar):
        self.grammar = grammar
    
    def parse(self, string):
        pass

if __name__ == '__main__':
    grammar_file = "grammar.txt"