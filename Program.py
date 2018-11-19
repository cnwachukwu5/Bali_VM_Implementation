import sys

from antlr4 import *
from BaliLexer import BaliLexer
from BaliParser import BaliParser
from AstVisitor import AstVisitor
from ByteCodeGenerator import ByteCodeGenerator
from ByteCodeUtility import ByteCodeUtility
from VirtualMachine import BaliVirtualMachine

def main(argv):
    input = FileStream(argv[1])
    lexer = BaliLexer(input)
    stream = CommonTokenStream(lexer)
    parser = BaliParser(stream)
    tree = parser.program()
    
    astVisitor = AstVisitor()
    astVisitor.visit(tree)
    # generate AST nodes
    astNode = astVisitor.programNode

    # generate byte code from the AST node
    bcg = ByteCodeGenerator()
    byte_code_list = bcg.visit(astNode)

    # execute the byte code
    vm = BaliVirtualMachine(byte_code_list)
    bcu = ByteCodeUtility(byte_code_list)

    #bcu.print(original = True)

    bcu.print(original = True)
    #bcu.print(original = False)
    #vm.run(debug=True)
    vm.run(debug=True)

if __name__ == '__main__':
    main(sys.argv)