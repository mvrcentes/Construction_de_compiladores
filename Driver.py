import sys
from antlr4 import *
from antlr4.tree.Trees import Trees
import graphviz

from lexer_parser.CompiScriptLanguageLexer import CompiScriptLanguageLexer
from lexer_parser.CompiScriptLanguageParser import CompiScriptLanguageParser

from semantic.SymbolGenerator import SymbolGenerator
from ir.TacGenerator import TacGenerator
from mips.CodeGenerator import CodeGenerator

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
    tree = parser.program()  # Start parsing from the 'program' rule in the grammar

    # Generate a DOT representation of the parse tree (if '--pdf' argument is provided)
    if len(argv) > 2 and argv[2] == '--pdf':
        dot_tree = generate_dot_tree(tree, parser.ruleNames)
        dot_tree.view('parse_tree', cleanup=True)
    else:
        # Create the symbol generator to walk the tree
        symbol_generator = SymbolGenerator()
        
        # Visit the tree to generate symbol tables
        context_manager = symbol_generator.visit(tree)

        # After visiting, check if there are any errors
        if symbol_generator.error_manager.has_errors():
            # If errors exist, print them
            symbol_generator.error_manager.display_errors()
        else:
            # If no errors, proceed to generate the intermediate code (TAC)
            tac_generator = TacGenerator(context_manager)
            tac_generator.visit(tree)

            code_generator = CodeGenerator("output.tac")
            mips_code = code_generator.generate_mips_code()

            # Print or write the MIPS code to a file
            for line in mips_code:
                print(line)

            code_generator.write_mips_to_file("output.asm")        

if __name__ == '__main__':
    main(sys.argv)

