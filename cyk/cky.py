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
        self.start = fi.readline().strip()
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
        table = [[[] for i in range (n + 1)] for j in range(n + 1) ]
        back = [[{} for i in range (n + 1)] for j in range(n + 1) ]
        # first loop
        for j in range(1, n + 1):
            for rule in self.grammar.productions:
                # 1st element is lhs of a rule, 2nd is the rhs
                if string[j-1] in rule[1]:
                    # if not table[j - 1][j]:
                    #     table[j - 1][j] = list()
                    table[j - 1][j].append(rule[0])
                    # append to backtrace
                    # back[j - 1][j].append(Node(rule, None, None, string[j - 1]))
        
        # loop over rows, backwards
        # adding an extra 1 because of the python range function
            for i in range(j-2, -1, -1):
                for k in range (i + 1, j):
                    for rule in self.grammar.productions:
                        for production in rule[1]:
                            if production.isupper():
                                # rule is of type A -> BC
                                if production[0] in table[i][k] and production[1] in table[k][j]:
                                    # if not table[i][j]:
                                    #     table[i][j] = list()
                                    table[i][j].append(rule[0])

                                    # add backtrace
                                    if rule[0] in back[i][j]:
                                        back[i][j][rule[0]].append((k, production[0], production[1]))
                                    else:
                                        back[i][j][rule[0]] = [(k, production[0], production[1])]
                                    # for b in back[i][k]:
                                    #     for c in back[k][j]:
                                    #         if b.root == production[0] and c.root == production[1]:
                                    #             back[i][j].append(Node(rule[0], b, c, None))

    
        return table, back
    

    def build_tree(self, back, table, i, j, label):
        start = back[i][j]
        trees = []
        # find the label if it is present in this start node.
        # print start, label
        if not start:
            # dict is empty, which means that this is a leaf node.
            for r in self.grammar.productions:
                if r[0] == label:
                    for t in r[1]:
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