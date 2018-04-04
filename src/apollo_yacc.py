# Yacc example
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from apollo_lex import tokens

#graphic AST stuff
import AST
from AST import addToClass
import sys
import pdb

def p_program2(p):
	'program2 : START NEWLINE program END NEWLINE'
	p[0] = p[3]
	
def p_program_statement_newline(p):
	'program : statement NEWLINE'
	p[0] = AST.ProgramNode(p[1])
		
def p_program_statement_program(p):
	'program : statement NEWLINE program'
	p[0] = AST.ProgramNode([p[1]] + [p[3]])

def p_statement_command(p):
	'statement : command'
	p[0] = p[1]

def p_statement_param(p):
	'statement : param'
	p[0] = p[1]

def p_statement_assignation(p):
	'statement : assignation'
	p[0] = p[1]
		
def p_param_AMP(p):
	'param : AMP TWOPOINTS INT'
	p[0] = AST.OpNode(p[1], [AST.TokenNode(p[3])])

def p_param_DUR(p):
	'param : DUR TWOPOINTS INT'
	p[0] = AST.OpNode(p[1], [AST.TokenNode(p[3])])

def p_command_param(p):
	'command : command COMMA param'
	p[0] = AST.ProgramNode([p[3], p[1]])
	
def p_command_PLAY(p):
	'command : PLAY TWOPOINTS LBRACKET expression RBRACKET'
	p[0] = AST.OpNode(p[1], [p[4]])

def p_assignation_expression(p):
	'assignation : VAR ID TWOPOINTS LBRACKET expression RBRACKET'
	p[0] = AST.OpNode(p[1], [AST.TokenNode(p[2]), p[5]])

def p_assignation(p):
	'assignation : VAR ID TWOPOINTS acc'
	p[0] = AST.OpNode(p[1], [AST.TokenNode(p[2]), p[4]])
		
def p_seqacc_acc(p):
    'expression : acc'
    p[0] = AST.OpNode('expression', [p[1]])

def p_seqacc_accseqacc(p):
    'expression : acc COMMA expression'
    p[0] = AST.OpNode('expression', [p[1], p[3]])

def p_acc_seqnotas(p):
    'acc : LPAREN seqnotas RPAREN'
    p[0] = AST.OpNode('acc', [p[2]])

def p_acc_nota(p):
    'acc : nota'
    p[0] = AST.OpNode('acc', [p[1]])

def p_seqnotas_nota(p):
    'seqnotas : nota'
    p[0] = AST.OpNode('seqnotas', [p[1]])

def p_seqnotas_notaseqnotas(p):
    'seqnotas : nota COMMA seqnotas'
    p[0] = AST.OpNode('seqnotas', [p[1], p[3]])

def p_nota_op(p):
	'''nota : nota SUM nota 
	| nota MINUS nota 
	| nota MULTIPLY nota'''
	
	p[0] = AST.OpNode(p[2], [p[1], p[3]])
	
def p_nota_int(p):
    'nota : INT'
    p[0] = AST.TokenNode(p[1])

def p_nota_id(p):
    'nota : ID'
    p[0] = AST.TokenNode(p[1])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc(debug=True)

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    prog = f.read()
    f.close()

    print("input:")
    print(prog)

    result = parser.parse(prog, debug = 1)
    print(result)

    graph = result.makegraphicaltree()
    graph.write_pdf('out.pdf')
