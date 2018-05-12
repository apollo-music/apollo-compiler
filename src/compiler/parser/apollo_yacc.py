# Yacc example
from ply.yacc import yacc

# Get the token map from the lexer.  This is required.
from ..lexer.apollo_lex import tokens
from ..exceptions import exceptions as exc

#graphic AST stuff
from ..AST import AST
from ..AST.AST import addToClass
import sys
import pdb

def p_program2(p):
	'program2 : START NEWLINE program END'
	p[0] = AST.EntryNode(p[3])
	
def p_program_statement_newline(p):
	'program : statement NEWLINE'
	p[0] = AST.ProgramNode(p[1])
		
def p_program_statement_program(p):
	'program : statement NEWLINE program'
	p[0] = AST.ProgramNode([p[1]] + [p[3]])

def p_statement(p):
	'''statement : command
		| param
		| assignation
		| loop'''
	p[0] = p[1]
		
def p_param_AMP(p):
	'param : AMP TWOPOINTS INT'
	p[0] = AST.AmpNode(AST.TokenNode(p[3]))

def p_param_DUR(p):
	'param : DUR TWOPOINTS INT'
	p[0] = AST.DurNode(AST.TokenNode(p[3]))

def p_param_INSTR(p):
	'param : INSTR TWOPOINTS INT'
	p[0] = AST.InstrNode(AST.TokenNode(p[3]))

def p_command_param(p):
	'command : command COMMA param'
	p[0] = AST.CommandNode([p[3], p[1]])
	
def p_command_PLAY(p):
	'command : PLAY TWOPOINTS LBRACKET seqexp RBRACKET'
	p[0] = AST.PlayNode([p[4]])

def p_assignation_expression(p):
	'assignation : VAR ID TWOPOINTS exp'
	p[0] = AST.VarNode([AST.TokenNode(p[2]), p[4]])

def p_expression_seq(p):
	'exp : LBRACKET seqsound RBRACKET rec_op'
	p[0] = AST.ExpressionNode([p[2], p[4]])

def p_expression_nota(p):
	'exp : nota rec_op'
	p[0] = AST.ExpressionNode([p[1], p[2]])

def p_expression_acc(p):
	'exp : acc rec_op'
	p[0] = AST.ExpressionNode([p[1], p[2]])

def p_seqexp_comma(p):
	'seqexp : exp COMMA seqexp'
	p[0] = AST.SeqexpNode([p[1], p[3]])

def p_seqexp(p):
	'seqexp : exp'
	p[0] = AST.SeqexpNode(p[1])

def p_recursive_op_empty(p):
	'rec_op : '
	p[0] = AST.EmptyNode()

def p_recursive_op_sum(p):
	'rec_op : SUM exp'
	p[0] = AST.OpNode(p[1], [p[2]])

def p_recursive_op_minus(p):
	'rec_op : MINUS exp'
	p[0] = AST.OpNode(p[1], [p[2]])

def p_recursive_op_ampersand(p):
	'rec_op : AMPERSAND exp'
	p[0] = AST.OpNode(p[1], [p[2]])

def p_seqsound_comma(p):
	'seqsound : sound COMMA seqsound'
	p[0] = AST.SeqsoundNode([p[1], p[3]])

def p_seqsound(p):
	'seqsound : sound'
	p[0] = AST.SeqsoundNode(p[1])

def p_sound(p):
	'''sound : acc
	| nota'''
	p[0] = AST.SoundNode(p[1])

def p_acc_seqnotas(p):
	'acc : LPAREN seqnotas RPAREN'
	p[0] = AST.AccNode([p[2]])

def p_seqnotas_nota(p):
	'seqnotas : nota'
	p[0] = AST.SeqNotasNode([p[1]])

def p_seqnotas_notaseqnotas(p):
	'seqnotas : nota COMMA seqnotas'
	p[0] = AST.SeqNotasNode([p[1], p[3]])

def p_nota(p):
	'nota : INT'
	p[0] = AST.TokenNode(p[1])

def p_nota_id(p):
	'nota : ID'
	p[0] = AST.TokenNode(p[1])

# def p_loop(p):
# 	'loop : repeat'
# 	p[0] = AST.LoopNode(p[1])

def p_loop_repeat(p):
	'loop : REPEAT INT TWOPOINTS NEWLINE program ENDREPEAT'
	p[0] = AST.RepeatNode([AST.TokenNode(p[2]), p[5]])

# Error rule for syntax errors
def p_error(p):
	print("\nSyntax error on line: %s" % (p.lineno))
	(AST.parser).errok()
	raise exc.MySyntaxError("Syntax error on line: %s" % (p.lineno))


def parse(program):
	'''
		Used to generate a AST parsing the program given as input
		USAGE: open the file with open and read it and use it as input to parse()
	'''
	AST.parser = yacc(debug=True)
	return (AST.parser).parse(program)

def run():
	AST.parser = yacc(debug=True)

	f = open(sys.argv[1], 'r')
	prog = f.read()
	f.close()

	print("input:")
	print(prog)

	result = (AST.parser).parse(prog, debug=1)
	print(result)

	graph = result.makegraphicaltree()
	graph.write_pdf('out.pdf')
