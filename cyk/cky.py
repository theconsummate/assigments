# -*- coding: utf-8 -*-

from sets import Set

class Grammar():
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
        self.new_symbols = ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


    def convert_to_cnf(self):
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
                    if production.isupper() and len(production) == 1:
                        # this is a unit production A -> B
                        # remove this
                        rhs.remove(production)
                        # add rules if not of type A -> A
                        if not production == lhs:
                            rhs += self.productions[production]

        def reduce_large_rules(self):
            # reduces large rules like A -> BCD to A -> XD and X -> BC
            # keep cache of reduced symbols and reuse the rules
            temp_symbols = {}
            for lhs, rhs in self.productions.items():
                for i in range(len(rhs)):
                    while True:
                        if len(rhs[i]) > 2:
                            current_val = rhs[i][:2]
                            # check cache
                            if current_val not in temp_symbols:
                                new_symbol = self.new_symbols.pop()
                                temp_symbols[current_val] = new_symbol
                            else:
                                new_symbol = temp_symbols[current_val]
                            # this should be reduced
                            rhs[i] = self.new_symbols.pop() + rhs[i][2:]
                            # add to productions dict
                            self.productions[new_symbol] = [current_val]
                            self.nonterminals.add(new_symbol)
                        else:
                            break
        

        def reduce_small_rules(self):
            # reduces small rules like A -> aB to A-> XB and X -> a
            # keep cache
            temp_symbols = {}
            for lhs, rhs in self.productions.items():
                for i in range(len(rhs)):
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
        print self.productions
        remove_null_productions(self)
        print self.productions
        remove_unit_productions(self)
        print self.productions
        reduce_large_rules(self)
        print self.productions
        reduce_small_rules(self)

    def read_grammar_file(self, filename):
        fi = open(filename)
        self.start = fi.readline().strip()
        for line in fi.readlines():
            # strip, remove whitespaces and then split into lhs and rhs
            lhs, rhs = line.strip().replace(" ", "").split("->")
            self.nonterminals.add(lhs)
            
            self.productions[lhs] = rhs.split("|")
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
        table = [[[] for i in range (n + 1)] for j in range(n + 1) ]
        back = [[{} for i in range (n + 1)] for j in range(n + 1) ]
        # first loop
        for j in range(1, n + 1):
            for lhs, rhs in self.grammar.productions.iteritems():
                # 1st element is lhs of a rule, 2nd is the rhs
                if string[j-1] in rhs:
                    # if not table[j - 1][j]:
                    #     table[j - 1][j] = list()
                    table[j - 1][j].append(lhs)
                    # append to backtrace
                    # back[j - 1][j].append(Node(rule, None, None, string[j - 1]))
        
        # loop over rows, backwards
        # adding an extra 1 because of the python range function
            for i in range(j-2, -1, -1):
                for k in range (i + 1, j):
                    for lhs, rhs in self.grammar.productions.iteritems():
                        for production in rhs:
                            if production.isupper():
                                # rule is of type A -> BC
                                if production[0] in table[i][k] and production[1] in table[k][j]:
                                    # if not table[i][j]:
                                    #     table[i][j] = list()
                                    table[i][j].append(lhs)

                                    # add backtrace
                                    if lhs in back[i][j]:
                                        back[i][j][lhs].append((k, production[0], production[1]))
                                    else:
                                        back[i][j][lhs] = [(k, production[0], production[1])]
                                    # for b in back[i][k]:
                                    #     for c in back[k][j]:
                                    #         if b.root == production[0] and c.root == production[1]:
                                    #             back[i][j].append(Node(lhs, b, c, None))

    
        return table, back
    

    def build_tree(self, back, table, i, j, label):
        start = back[i][j]
        trees = []
        # find the label if it is present in this start node.
        # print start, label
        if not start:
            # dict is empty, which means that this is a leaf node.
            for lhs, rhs in self.grammar.productions.iteritems():
                if lhs == label:
                    for t in rhs:
                        if t.islower():
                            return [label + "{" + t + "}"]
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
    string = "baaba"
    grammar_file = "grammar.txt"
    grammar = Grammar()
    grammar.read_grammar_file(grammar_file)
    grammar.convert_to_cnf()
    print grammar
    parser = CKYParser(grammar)
    table, back = parser.parse(string)
    for row in table:
        print row
    print "$$$$$$$$$$$$$$$"
    for row in back:
        print row
    print(table[0][len(string)])
    print back[0][len(string)]
    print parser.build_tree(back, table, 0, len(string), grammar.start )
    # print table
    # print back
    # printParseTrees(back[0][5])