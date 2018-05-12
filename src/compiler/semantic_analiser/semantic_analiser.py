import sys
from ..AST import AST
from ..AST.AST import addToClass
from ..AST.AST import Node
from ..exceptions import exceptions

## Testes a serem feitos
# - Passar variável no amp, dur, instr
# - Verificar se nome dentro de acc é uma sequencia de musica (nao pode acontecer ouch = [3,4] e play: [1, (2, ouch), 5])

AST.ScopeStack = []

###############
# Op on Stack #
###############
def getCurrentScope():
	return AST.ScopeStack[-1]

def pushScope(scp, dependency=None):
	if dependency is None:
		d = len(AST.ScopeStack) - 1 if len(AST.ScopeStack) > 0 else 0
		scp.setDependency(d)
	else:
		scp.setDependency(dependency)
	
	AST.ScopeStack.append(scp)

def popScope():
	AST.ScopeStack.pop()

def findSymbol(symbol):
	# print('DEBUG: Finding ' + str(symbol))
	currentScope = len(AST.ScopeStack) - 1

	while currentScope is not None:
		# print('DEBUG: \tSearchin on scope ' + str(currentScope))
		# Get the scope on
		scope_symbol = AST.ScopeStack[currentScope].isInScope(symbol)
		if scope_symbol:
			return scope_symbol

		if AST.ScopeStack[currentScope].dep == currentScope:
			return False

		currentScope = AST.ScopeStack[currentScope].dep

def insertSymbol(symbol, value):
	scp = getCurrentScope()
	scp.addDefiniton(symbol, value)

###############
# Scope class #
###############
class Scope():
	'''
		The scope class defines a scope holding the value of the variables
		ans which scopes the scope can access
	'''
	def __init__(self, name):
		'''
			dep: dep is a int position on the stack
		'''
		self.name = name
		self.dep = 0
		self.dfn = dict()

	def __str__(self):
		return (self.name + '-' + str(self.dep))
	
	def __repr__(self):
		return (self.name + ' ' + str(self.dep) + str(self.dfn) + '\n') 

	def setDependency(self, dep):
		self.dep = dep

	def addDefiniton(self, key, value):
		self.dfn[key] = value

	def isInScope(self, key):
		return self.dfn.get(key, False)


########################
## Analiser Functions ##
########################
# GenericNode - Default
@addToClass(AST.Node)
def analise(self):
	for c in self.children:
		c.analise()
	return self

# EntryNode (First node of program)
# - 'program2 : START NEWLINE program END NEWLINE' | AST.EntryNode(p[3])
@addToClass(AST.EntryNode)
def analise(self):
	print('DEBUG: ' + str(self))
	pushScope(Scope('global'), 0) # Global scope has scope 0
	c = self.children[0].analise()
	# print('DEBUG: ' + str(c))
	return c

# ProgramNode (generic)
# - 'program : statement NEWLINE' | AST.ProgramNode(p[1])
# - 'program : statement NEWLINE program' | AST.ProgramNode([p[1]] + [p[3]])
# '''statement : command | param | assignation | loop'''
@addToClass(AST.ProgramNode)
def analise(self):
	# print("DEBUG: Creating scope program: " + str(len(AST.ScopeStack)))
	pushScope(Scope('program_' + str(len(AST.ScopeStack))))
	
	statement = [self.children[0].analise()]
	if len(self.children) > 1:
		program = self.children[1].analise()
		statement = statement + program
	
	popScope()
	# print("DEBUG: Popping scope program: " + str(len(AST.ScopeStack)))
	
	return statement

# AmpNode
# - 'param : AMP TWOPOINTS INT' | AST.AmpNode([AST.TokenNode(p[3])])
@addToClass(AST.AmpNode)
def analise(self):
	amp = self.children[0].analise()
	insertSymbol('AMP', amp)
	return amp

# DurNode
# - 'param : DUR TWOPOINTS INT' | AST.DurNode([AST.TokenNode(p[3])])
@addToClass(AST.DurNode)
def analise(self):
	dur = self.children[0].analise()
	insertSymbol('DUR', dur)
	return dur

# InstrNode
# - 'param : INSTR TWOPOINTS INT' | AST.InstNode([AST.TokenNode(p[3])])
@addToClass(AST.InstrNode)
def analise(self):
	ins = self.children[0].analise()
	insertSymbol('INSTR', ins)
	return ins

# CommandNode
# - ' : command COMMA param' | AST.CommandNode([p[3], p[1]])
@addToClass(AST.CommandNode)
def analise(self):
	pushScope(Scope('comand_' + str(len(AST.ScopeStack))))
	# print("DEBUG: Creating scope comand: " + str(len(AST.ScopeStack)))
	
	command = [self.children[0].analise()]
	param = self.children[1].analise()
	
	popScope()
	# print("DEBUG: Popping scope comand: " + str(len(AST.ScopeStack)))
	return command + param

# PlayNode
# 'command : PLAY TWOPOINTS LBRACKET seqsound RBRACKET' | AST.PlayNode([p[4]])
@addToClass(AST.PlayNode)
def analise(self):
	# Check if amp, dur, and instruments are declared on the scope
	exists_amp = findSymbol('AMP')
	exists_dur = findSymbol('DUR')
	exists_inst = findSymbol('INSTR')
	# print('DEBUG: Check amp, dur and inst')
	# print(exists_amp, exists_dur, exists_inst)

	if not exists_amp:
		print("Atention, no Aplitute defined on the scope, using default;")
	if not exists_dur:
		print("Atention, no Duration defined on the scope, using default;")
	if not exists_inst:
		print("Atention, no Instrument defined on the scope, using default;")

	seqsound = self.children[0].analise()
	return seqsound

# VarNode
# 'assignation : VAR ID TWOPOINTS exp' | AST.VarNode([AST.TokenNode(p[2]), p[4]])
@addToClass(AST.VarNode)
def analise(self):
	ID = self.children[0].analise()
	exp = self.children[1].analise()
	insertSymbol(ID, exp)
	return self

# ExpressionNode
# - 'exp : LBRACKET seqsound RBRACKET rec_op' |  AST.ExpressionNode([p[2], p[4]])
# - 'exp : nota rec_op'| AST.ExpressionNode([p[1], p[2]])
# - 'exp : acc rec_op' | AST.ExpressionNode([p[1], p[2]])
@addToClass(AST.ExpressionNode)
def analise(self):
	left = self.children[0].analise()
	# print('DEBUG: ExpressionNode left: ' + str(left))
	right = self.children[1].analise()
	# print('DEBUG: ExpressionNode right: ' + str(right))

	return [left, right]

# OpNode
# 'rec_op : SUM exp' |  AST.OpNode(p[1], [p[2]])
# 'rec_op : MINUS exp' | AST.OpNode(p[1], [p[2]])
@addToClass(AST.OpNode)
def analise(self):
	# print('DEBUG: AST.OpNode', str(self))
	op = self.children[0].analise()
	exp = self.children[1].analise()
	return [op, exp]


# SeqSoundNode
# 'seqsound : sound COMMA seqsound' | AST.SeqsoundNode([p[1], p[3]])
# 'seqsound : sound' | AST.SeqsoundNode(p[1])
@addToClass(AST.SeqsoundNode)
def analise(self):
	if len(self.children) > 1:
		sound = self.children[0].analise()
		seqsound = self.children[1].analise()
		return [sound] + seqsound
	else:
		sound = self.children[0].analise()
		return [sound]

# SoundNode
# 	'''sound : acc | nota''' | AST.SoundNode(p[1])
@addToClass(AST.SoundNode)
def analise(self):
	acc_or_nota = self.children[0].analise()
	if type(acc_or_nota) is str:
		if not findSymbol(acc_or_nota):
			print("Error: %s used but never was defined" % (acc_or_nota))
			# Should break the program? idn
	
	return acc_or_nota

# AccNode
# 'acc : LPAREN seqnotas RPAREN' | AST.AccNode([p[2]])
@addToClass(AST.AccNode)
def analise(self):
	# PRECISA COLOCAR QUE ESSA SEQ DE NOTAS É ACORDE
	seq_notas = self.children[0].analise()
	return tuple(seq_notas)

# SeqNotasNode
# 'seqnotas : nota' | AST.SeqNotasNode([p[1]])
# 'seqnotas : nota COMMA seqnotas' | AST.SeqNotasNode([p[1], p[3]])
@addToClass(AST.SeqNotasNode)
def analise(self):
	nota = self.children[0].analise()
	# print(type(nota), nota)
	if type(nota) is str:
		if not findSymbol(nota):
			print("Error: %s used but never was defined" % (nota))
			# Should break the program? idn

	ret = [nota]
	seqNotas = []
	if len(self.children) > 1:
		seqNotas = self.children[1].analise()

	return ret + seqNotas

# TokenNode ()
@addToClass(AST.TokenNode)
def analise(self):
	return self.tok

# RepeatNode
# 'loop : REPEAT INT TWOPOINTS NEWLINE program ENDREPEAT' | AST.RepeatNode([AST.TokenNode(p[2]), p[5]])
@addToClass(AST.RepeatNode)
def analise(self):
	return self

# EmptyNode
# 'rec_op : ' | AST.EmptyNode()
@addToClass(AST.EmptyNode)
def analise(self):
	return []


## This is the function to execute the semantic analiser
def run(ast):
	ast.analise()
	#print("Semantic Analisys Completed...")


def test():
	import sys
	import os
	from compiler.parser import apollo_yacc

	f = open(sys.argv[1], 'r')
	prog = f.read()
	f.close()

	try:
		# Generate ast
		ast = apollo_yacc.parse(prog)
	except:
		print(sys.exc_info()[0])

	try:
		# Run semantic analysis
		run(ast)
	except:
		print(sys.exc_info()[0])
