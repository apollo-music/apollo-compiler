# Yacc example
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calclex import tokens

#graphic AST stuff
import AST
import sys

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

def p_expression_term(p):
    'expression : term'
    p[0] = AST.TokenNode(p[1])

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

def p_term_factor(p):
    'term : factor'
    p[0] = AST.TokenNode(p[1])

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = AST.TokenNode(p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = AST.OpNode(p[1], [p[2], p[3]])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc(outputdir='generated')

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
