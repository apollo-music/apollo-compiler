## Apollo music gen semantic analysiss
# This semantic analysis do:
# - Scope checkin: Variables are declared before using it
#    - Checks variables
#    - Checks amp, dur and instr
#    - MISSING REPEAT						- TODO
# - Valid var use: Check if a var is used an inalid place
#    - Cannot use ouch = [3,4] e play: [1, (2, ouch), 5]
# - Operation on riht types
#    - Length of types are wrong			- TODO
#    - Types are wrong   					- TODO
## Testes que estão sendo feitos
# - Passar variável no amp, dur, instr  - NOT WORKING
import sys
from ..AST import AST
from ..AST.AST import addToClass
from ..AST.AST import Node
from ..exceptions import exceptions

###############
# Scope class #
###############
class Scope():
	'''
		The scope class defines a scope holding the value of the variables
		ans which scopes the scope can access - the dep is an hierarch level dep
		so if you can access b, you can access dep b and so on
	'''
	def __init__(self, name):
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


###############
# Op on Stack #
###############
AST.ScopeStack = []

def getCurrentScope():
	'''
		returns the last scope on the scope stack
	'''
	return AST.ScopeStack[-1]

def pushScope(scp, dependency=None):
	'''
		Inserts an element (scp) on ScopeStack
		and automatically defines its dependency on the last
	'''
	if dependency is None:
		d = len(AST.ScopeStack) - 1 if len(AST.ScopeStack) > 0 else 0
		scp.setDependency(d)
	else:
		scp.setDependency(dependency)

	AST.ScopeStack.append(scp)

def popScope():
	'''
		Removes the last scope
	'''
	AST.ScopeStack.pop()

def findSymbol(symbol):
	'''
		Seach for symbol on all the scope hiearachy
	'''
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
# 'command : PLAY TWOPOINTS playcontent' | AST.PlayNode([p[3]])
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
	print(seqsound)
	return seqsound

# PlaycontentNode
# 'playcontent : LBRACKET seqexp RBRACKET' | AST.PlaycontentNode([p[2]])
# 'playcontent : ID'  | AST.PlaycontentNode(AST.TokenNode(p[1]))
# 'playcontent : acc' | AST.PlaycontentNode(p[1])
@addToClass(AST.PlaycontentNode)
def analise(self):
	play_val = self.children[0].analise()

	# Check if its an ID
	if type(play_val) is str:
		var_val = findSymbol(play_val)
		if not var_val:
			print("Error: %s used but never was defined" % (play_val))
			# Should break the program? idn
		else:
			return var_val
	
	return play_val

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

	## Checking if nota is a variable
	if type(left) is str:
		var_val = findSymbol(left)
		if not var_val:
			print("Error: %s used but never was defined" % (left))
			# Should break the program? idn
		else:
			return var_val

	rec_op = self.children[1].analise()
	if not rec_op:
		return left
	# print('DEBUG: ExpressionNode rec_op: ' + str(rec_op))

	return [left + rec_op]

# SeqexpNode
# 'seqexp : exp COMMA seqexp' | AST.SeqexpNode([p[1], p[3]])
# 'seqexp : exp' | AST.SeqexpNode(p[1])
@addToClass(AST.SeqexpNode)
def analise(self):
	exp = self.children[0].analise()

	# print('DEBUG exp ' + str(exp))

	if len(self.children) > 1:
		segexp = self.children[1].analise()
		# print('DEBUG segexp ' + str(segexp))
		return [exp, segexp]

	return exp

# OpNode
# 'rec_op : SUM exp' |  AST.OpNode(p[1], [p[2]])
# 'rec_op : MINUS exp' | AST.OpNode(p[1], [p[2]])
# 'rec_op : AMPERSAND exp'
@addToClass(AST.OpNode)
def analise(self):
	# NEEDS IMPLEMENTATION
	# print('DEBUG: AST.OpNode', str(self))
	op = self.op
	val = self.children[0].analise()
	return [op, val]


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

	## Checking if nota is a variable
	if type(acc_or_nota) is str:
		var_val = findSymbol(acc_or_nota)
		if not var_val:
			print("Error: %s used but never was defined" % (acc_or_nota))
			# Should break the program? idn
		else:
			return var_val
	
	return acc_or_nota

# AccNode
# 'acc : LPAREN seqnotas RPAREN' | AST.AccNode([p[2]])
@addToClass(AST.AccNode)
def analise(self):
	seq_notas = self.children[0].analise()

	# Analise seq_notas e ver se tem algum elemtno tipo lista
	# se tiver é por que existe uma variavel tipo [] dento do ()
	for e in seq_notas:
		if type(e) is list:
			print('Error: Invalid type inside a chord\n Check the variable values')
			sys.exit(1)

	return tuple(seq_notas)

# SeqNotasNode
# 'seqnotas : nota' | AST.SeqNotasNode([p[1]])
# 'seqnotas : nota COMMA seqnotas' | AST.SeqNotasNode([p[1], p[3]])
@addToClass(AST.SeqNotasNode)
def analise(self):
	nota = self.children[0].analise()

	## Checking if nota is a variable
	if type(nota) is str:
		var_val = findSymbol(nota)
		if not var_val:
			print("Error: %s used but never was defined" % (nota))
			# Should break the program? idn
		else:
			nota = var_val

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
	return False


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
