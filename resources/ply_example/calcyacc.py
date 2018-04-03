# Yacc example
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calclex import tokens

#graphic AST stuff
import AST
from AST import addToClass
import sys
import pdb

def p_play_seq(p):
    'p_play : PLAY TWOPOINTS LBRACKET seqacc RBRACKET'
    p[0] = AST.OpNode(p[1],[p[4]])

def p_seqacc_acc(p):
    'seqacc : acc'
    p[0] = p[1]

def p_seqacc_accseqacc(p):
    'seqacc : acc COMMA seqacc'
    p[0] = AST.TokenNode(0)
    p[0].tok = p[1].tok + ", " + p[3].tok

def p_acc_seqnotas(p):
    'acc : LPAREN seqnotas RPAREN'
    p[0] = AST.TokenNode(0)
    p[0].tok = "( " + p[2].tok + " )"

def p_acc_nota(p):
    'acc : nota'
    p[0] = p[1]

def p_seqnotas_nota(p):
    'seqnotas : nota'
    p[0] = p[1]

def p_seqnotas_notaseqnotas(p):
    'seqnotas : nota COMMA seqnotas'
    p[0] = AST.TokenNode(0)
    p[0].tok = p[1].tok + " , " + p[3].tok

def p_nota_int(p):
    'nota : INT'
    p[0] = AST.TokenNode(str(p[1]))

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    prog = f.read()
    f.close()

    print("input:")
    print(prog)

    result = parser.parse(prog)
    print(result)

    graph = result.makegraphicaltree()
    graph.write_pdf('out.pdf')
