import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
import graphviz

from lexer_parser.CompiScriptLanguageLexer import CompiScriptLanguageLexer
from lexer_parser.CompiScriptLanguageParser import CompiScriptLanguageParser

from semantic.SymbolGenerator import SymbolGenerator

def generate_dot_tree(tree, rule_names):
    """Generate a DOT representation of the parse tree."""
    def to_dot(node, dot=None):
        if dot is None:
            dot = graphviz.Digraph(comment='Parse Tree')
        
        # Get the name of the node (either a rule or a token)
        node_name = Trees.getNodeText(node, rule_names)
        node_id = str(id(node))  # Unique ID for the node

        # Add the node to the graph
        dot.node(node_id, label=node_name)

        # Recursively add child nodes
        for child in range(node.getChildCount()):
            child_node = node.getChild(child)
            child_id = str(id(child_node))
            dot.edge(node_id, child_id)
            to_dot(child_node, dot)

        return dot

    return to_dot(tree)

def main(argv):
    input_file = argv[1]
    with open(input_file, encoding='utf-8') as file:
        input_stream = InputStream(file.read())

    lexer = CompiScriptLanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CompiScriptLanguageParser(stream)
    tree = parser.program()  # We are using 'program' since this is the starting rule based on our CompiScriptLanguage grammar

    # Generate a DOT representation of the parse tree
    if len(argv) > 2 and argv[2] == '--pdf':
        dot_tree = generate_dot_tree(tree, parser.ruleNames)
        # dot_tree.render('parse_tree', format='pdf', cleanup=True)
        dot_tree.view('parse_tree', cleanup=True)

    else:
        # Generate the symbols tables
        symbol_generator = SymbolGenerator()
        symbol_generator.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
