# -*- coding: utf-8 -*-

from sets import Set
import sys

"""
This module implements the CYK table parsing algorithm.
Usage:

python cyk.py grammar_file "sentence with words separate by white spaces"
"""

def is_production_terminal(production):
    """
    Args
    production: an array containing the elements of the rhs of a rule.

    returns:
    True if the char ' is found in any for the element. False otherwise
    """
    for p in production:
        if "'" in p:
            return True
    return False


class Grammar():
    """
    This is the init method, inits an empty grammar object
    """
    def __init__(self):
        # define null production
        self.null = "ε"
        # all upper case symbols
        self.nonterminals = Set()
        # all lowercase symbols
        self.terminals = Set()
        # this will be a list of tuples with lhs as the first element and rhs as an array of outputs
        self.productions = {}
        self.start = list()
        # TODO: hack for now, maybe this will be sufficient !!
        self.new_symbols = ["J", "K", "Q", "R", "T", "U", "W", "X", "Y", "Z"]


    def convert_to_cnf(self):
        """
        This method converts the object into a CNF grammar. The various steps are implemented in their own sub-methods.
        """
        def eliminate_start_symbol_from_rhs(self):
            for lhs, rhs in self.productions.items():
                for production in rhs:
                    if self.start in production:
                        # start symbol is present in rhs, create a new start symbol
                        self.start += "0"
                        # drop the last char and we will have the original start symbol
                        self.productions[self.start] = [self.start[:-1]]
                        # add to list of non-terminals
                        self.nonterminals.add(self.start)
                        break
        
        def remove_null_productions(self):
            null_list = list()
            for lhs, rhs in self.productions.items():
                # rhs[:] = [x for x in rhs if x == self.null and lhs not in null_list]
                for production in rhs:
                    if production == self.null and lhs not in null_list:
                        null_list.append(lhs)
                        rhs.remove(production)
                    if production in null_list:
                        # ripple effect of another rule being null
                        null_list.append(lhs)
                # if after this null removal, there are no productions for a given rule, remove that rule.
                if len(rhs) == 0:
                    del self.productions[lhs]
                    # TODO remove from non terminal list also
 
            # propagate the null values to other rules
            for val in null_list:
                for lhs, rhs in self.productions.items():
                    for production in rhs:
                        # if the val is in the rhs and it still has a non - null production
                        if val in production and val in self.productions:
                            strr = production.replace(val, "")
                            if not strr == "":
                                rhs.append(strr)

        def remove_unit_productions(self):
            for lhs, rhs in self.productions.items():
                for production in rhs:
                    if not is_production_terminal(production) and len(production) == 1:
                        # this is a unit production A -> B
                        # remove this
                        rhs.remove(production)
                        # add rules if not of type A -> A
                        if not production[0] == lhs:
                            rhs += self.productions[production[0]]

        def reduce_large_rules(self):
            # reduces large rules like A -> BCD to A -> XD and X -> BC
            # keep cache of reduced symbols and reuse the rules
            temp_symbols = {}
            for lhs, rhs in self.productions.items():
                for i in range(len(rhs)):
                    while True:
                        if len(rhs[i]) > 2:
                            current_val = rhs[i][:2]
                            cache_key = ','.join(current_val)
                            # check cache, convert to a string before key
                            if cache_key not in temp_symbols:
                                new_symbol = self.new_symbols.pop()
                                temp_symbols[cache_key] = new_symbol
                            else:
                                new_symbol = temp_symbols[cache_key]
                            # this should be reduced
                            rhs[i] = [new_symbol] + rhs[i][2:]
                            # add to productions dict
                            self.productions[new_symbol] = [current_val]
                            self.nonterminals.add(new_symbol)
                        else:
                            break
        

        def reduce_small_rules(self):
            # removes terminals cooccuring with nonterminals
            # reduces small rules like A -> aB to A-> XB and X -> a
            # keep cache
            temp_symbols = {}
            for lhs, rhs in self.productions.items():
                for i in range(len(rhs)):
                    if is_production_terminal(rhs[i]):
                        # this means that there is only a terminal symbol here
                        continue
                    for j in range(len(rhs[i])):
                        if rhs[i][j].islower():
                            current_val = rhs[i][j]
                            # check cache
                            if current_val not in temp_symbols:
                                new_symbol = self.new_symbols.pop()
                                temp_symbols[current_val] = new_symbol
                            else:
                                new_symbol = temp_symbols[current_val]
                            # update current rule
                            rhs[i] = rhs[i][:j] + new_symbol + rhs[i][j+1:]
                            # add new rule
                            self.productions[new_symbol] = [current_val]


        eliminate_start_symbol_from_rhs(self)
        # print self.productions
        remove_null_productions(self)
        # print self.productions
        remove_unit_productions(self)
        # print self.productions
        reduce_large_rules(self)
        # print self.productions
        reduce_small_rules(self)

    def read_grammar_file(self, filename):
        """
        reads a given grammar file and loads the information into self.
        """
        fi = open(filename)
        self.start = fi.readline().strip()
        for line in fi.readlines():
            # strip, remove whitespaces and then split into lhs and rhs
            lhs, rhs = line.strip().split("->")
            lhs = lhs.strip()
            rhs = rhs.strip()
            self.nonterminals.add(lhs)
            
            if lhs not in self.productions:
                self.productions[lhs] = []
            self.productions[lhs] += [p.strip().split(" ") for p in rhs.split("|")]
            # iterate the elements of rhs and add the small case chars to terminals
            # TODO this is not correct
            for c in rhs.split("|"):
                if c.islower():
                    self.terminals.add(c)
    
    
    def __str__(self):
        return "non-terminals: " + str(self.nonterminals) + "\nterminals: " + str(self.terminals) + "\nproductions:" + str(self.productions)


"""
Pseudo code:

"""
class CYKParser():
    """
    constructor for the parser class.
    """
    def __init__(self, grammar):
        self.grammar = grammar
    
    def parse(self, string):
        """
        parse a given string using the grammar with which this class was initialized.

        Args:
        string: an array of words which has to be parsed.

        Returns:
        table: a table containing the CYK chart
        back: a table containing the corresponding back pointers to build the parse tree.
        """
        n = len(string)
        # init matrix of size (n+1, n+1)
        table = [[[] for i in range (n + 1)] for j in range(n + 1) ]
        back = [[{} for i in range (n + 1)] for j in range(n + 1) ]
        # first loop
        for j in range(1, n + 1):
            for lhs, rhs in self.grammar.productions.iteritems():
                # 1st element is lhs of a rule, 2nd is the rhs
                for element in rhs:
                    if string[j-1] in element:
                        # if not table[j - 1][j]:
                        #     table[j - 1][j] = list()
                        table[j - 1][j].append(lhs)
                        # add the back pointer here
                        back[j - 1][j] = string[j-1]
        
        # loop over rows, backwards
        # adding an extra 1 because of the python range function
            for i in range(j-2, -1, -1):
                for k in range (i + 1, j):
                    for lhs, rhs in self.grammar.productions.iteritems():
                        for production in rhs:
                            if not is_production_terminal(production):
                                # rule is of type A -> BC
                                # print production
                                # print (i,j,k)
                                if production[0] in table[i][k] and production[1] in table[k][j]:
                                    # if not table[i][j]:
                                    #     table[i][j] = list()
                                    table[i][j].append(lhs)

                                    # add backtrace
                                    if lhs in back[i][j]:
                                        back[i][j][lhs].append((k, production[0], production[1]))
                                    else:
                                        back[i][j][lhs] = [(k, production[0], production[1])]

    
        return table, back
    

    def build_tree(self, back, table, i, j, label):
        """
        Builds a parse tree recursively for a given parse and a given start symbol.

        Args:
        back: a table containing back pointers, as returned from the parse method
        table: a table containing CYK chart, as returned from the parse method
        i: start row index
        j: start column index
        label: start symbol

        Returns:
        trees: an array containing all the possible parse trees.
        """
        start = back[i][j]
        trees = []
        # find the label if it is present in this start node.
        # print start, label
        if type(start) is str:
            # this is a leaf node
            return [label + "{" + start + "}"]
            # dict is empty, which means that this is a leaf node.
            # for lhs, rhs in self.grammar.productions.iteritems():
            #     if lhs == label:
            #         for t in rhs:
            #             if is_production_terminal(t):
            #                 return [label + "{" + t[0] + "}"]
        else:
            # this is not a leaf node, find the label in the current node and print out the children
            if label in start:
                for path in start[label]:
                    left = self.build_tree(back, table, i, path[0], path[1])
                    right = self.build_tree(back, table, path[0], j, path[2])
                    for l in left:
                        for r in right:
                            if l and r:
                                tree = "(" + label + "$ (" + l + " " + r + ") #)"
                                trees.append(tree)
        return trees

if __name__ == '__main__':
    if len(sys.argv) == 3:
        grammar_file = sys.argv[1]
        string = sys.argv[2]
    else:
        # use default
        string = "Batman slept on the street"
        string = "Batman ate an apple"
        string = "Batman ate an apple on the street"
        # string = "a b"
        grammar_file = "grammar2.txt"
    # split the string into an array of words
    string = ["'" + s + "'" for s in string.split(" ")]
    grammar = Grammar()
    grammar.read_grammar_file(grammar_file)
    # printing before conversion
    print grammar
    grammar.convert_to_cnf()
    print grammar
    parser = CYKParser(grammar)
    table, back = parser.parse(string)
    for row in table:
        print row
    print "$$$$$$$$$$$$$$$"
    for row in back:
        print row
    print(table[0][len(string)])
    print back[0][len(string)]
    parses = parser.build_tree(back, table, 0, len(string), grammar.start )
    for p in parses:
        print p
        print "###"
    # print table
    # print back
    # printParseTrees(back[0][5])