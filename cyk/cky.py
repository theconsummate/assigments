from sets import Set

class Grammar():
    def __init__(self):
        # all upper case symbols
        self.nonterminals = Set()
        # all lowercase symbols
        self.terminals = Set()
        # this will be a list of tuples with lhs as the first element and rhs as an array of outputs
        self.productions = list()
        self.start = list()

    def convert_to_cnf(self):
        pass


    def read_grammar_file(self, filename):
        fi = open(filename)
        for line in fi.readlines():
            # strip, remove whitespaces and then split into lhs and rhs
            lhs, rhs = line.strip().replace(" ", "").split("->")
            self.nonterminals.add(lhs)
            
            self.productions.append((lhs, rhs.split("|")))
            # iterate the elements of rhs and add the small case chars to terminals
            for c in rhs.split("|"):
                if c.islower():
                    self.terminals.add(c)
    
    
    def __str__(self):
        return "non-terminals: " + str(self.nonterminals) + "\nterminals: " + str(self.terminals) + "\nproductions:" + str(self.productions)


"""
Pseudo code:

"""
class CKYParser():
    """
    constructor for the parser class.
    """
    def __init__(self, grammar):
        self.grammar = grammar
    
    def parse(self, string):
        n = len(string)
        # init matrix of size (n+1, n+1)
        table = [[None for i in range (n + 1)] for j in range(n + 1) ]
        # first loop
        for j in range(1, n + 1):
            for rule in self.grammar.productions:
                # 1st element is lhs of a rule, 2nd is the rhs
                if string[j-1] in rule[1]:
                    if not table[j - 1][j]:
                        table[j - 1][j] = list()
                    table[j - 1][j].append(rule[0])
        
        # loop over rows, backwards
        # adding an extra 1 because of the python range function
            for i in range(j-2, -1, -1):
                for k in range (i + 1, j):
                    print (j, i, k)
                    for rule in self.grammar.productions:
                        for production in rule[1]:
                            if production.isupper():
                                # rule is of type A -> BC
                                if table[i][k] and production[0] in table[i][k] and table[k][j] and production[1] in table[k][j]:
                                    if not table[i][j]:
                                        table[i][j] = list()
                                    table[i][j].append(rule[0])

    
        return table


if __name__ == '__main__':
    grammar_file = "grammar.txt"
    grammar = Grammar()
    grammar.read_grammar_file(grammar_file)
    print grammar
    parser = CKYParser(grammar)
    table = parser.parse("baaba")
    for row in table:
        print row
    print(table[0][5])