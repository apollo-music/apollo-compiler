import sys
from ..AST import AST
from ..AST.AST import addToClass
from ..AST.AST import Node
from ..exceptions import exceptions


AST.ScopeStack = []

###############
# Op on Stack #
###############
def getCurrentScope():
	return AST.ScopeStack[-1]

def pushScope(scope):
	AST.ScopeStack.append(scope)

def popScope():
	AST.ScopeStack.pop()

def findSymbol(symbol):
	currentScope = len(AST.ScopeStack) - 1

	while currentScope is not None:
		scope_symbol = AST.ScopeStack[currentScope].isInScope(symbol)
		if scope_symbol:
			return scope_symbol

		if AST.ScopeStack[currentScope].dependency == currentScope:
			return False

		currentScope = AST.ScopeStack[currentScope].dependency

def insertSymbol(symbol, value):
	getCurrentScope().addDefiniton(symbol, value)

###############
# Scope class #
###############
class Scope():
	'''
		The scope class defines a scope holding the value of the variables
		ans which scopes the scope can access
	'''
	name = ""
	dependency = 0 		## This is not in use as theres no scolpe multlevel
	definitions = {}
	
	def __init__(self, name, dependency=0, definitions={}):
		'''
			depency: dependencie is a int position on the stack
		'''
		self.name = name
		if dependency is not None:
			self.dependency = dependency
		if definitions is not None:
			self.definitions = definitions
	
	def __str__(self):
		return (self.name + str(self.dependency) + str(self.definitions))
		
	def addDefiniton(self, key, value):
		self.definitions[key] = value
	
	def isInScope(self, key):
		self.definitions.get(key, False)


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
	pushScope(Scope('global'))
	c = self.children[0]
	return c.analise()

# ProgramNode (generic)
# - 'program : statement NEWLINE' | AST.ProgramNode(p[1])
# - 'program : statement NEWLINE program' | AST.ProgramNode([p[1]] + [p[3]])
@addToClass(AST.ProgramNode)
def analise(self):
	for c in self.children:
		c.analise()
	return self

# AmpNode
# - 'param : AMP TWOPOINTS INT' | AST.AmpNode([AST.TokenNode(p[3])])
@addToClass(AST.AmpNode)
def analise(self):
	return self.children[0].analise()

# DurNode
# - 'param : DUR TWOPOINTS INT' | AST.DurNode([AST.TokenNode(p[3])])
@addToClass(AST.DurNode)
def analise(self):
	return self.children[0].analise()

# InstrNode
# - 'param : INSTR TWOPOINTS INT' | AST.InstNode([AST.TokenNode(p[3])])
@addToClass(AST.InstrNode)
def analise(self):
	return self.children[0].analise()

# CommandNode
# - 'command : command COMMA param' | AST.CommandNode([p[3], p[1]])
@addToClass(AST.CommandNode)
def analise(self):
	for c in self.children:
		c.analise()
	return self

# PlayNode
# 'command : PLAY TWOPOINTS LBRACKET seqsound RBRACKET' | AST.PlayNode([p[4]])
@addToClass(AST.PlayNode)
def analise(self):
	exp = self.children[0].analise()

# VarNode
# 'assignation : VAR ID TWOPOINTS exp' | AST.VarNode([AST.TokenNode(p[2]), p[4]])
@addToClass(AST.VarNode)
def analise(self):
	ID = self.children[0]
	exp = self.children[1].analise()

	insertSymbol(ID, exp)

	return self

# ExpressionNode
# - 'exp : LBRACKET seqsound RBRACKET rec_op' |  AST.ExpressionNode([p[2], p[4]])
# - 'exp : nota rec_op'| AST.ExpressionNode([p[1], p[2]])
# - 'exp : acc rec_op' | AST.ExpressionNode([p[1], p[2]])
@addToClass(AST.ExpressionNode)
def analise(self):
	for c in self.children:
		c.analise()
	return self

# OpNode
# 'rec_op : SUM exp' |  AST.OpNode(p[1], [p[2]])
# 'rec_op : MINUS exp' | AST.OpNode(p[1], [p[2]])
@addToClass(AST.OpNode)
def analise(self):
	return self

# SeqSoundNode
# 'seqsound : sound COMMA seqsound' | AST.SeqsoundNode([p[1], p[3]])
# 'seqsound : sound' | AST.SeqsoundNode(p[1])
@addToClass(AST.SeqsoundNode)
def analise(self):
	return self.tok

# SoundNode
# 	'''sound : acc | nota''' | AST.SoundNode(p[1])
@addToClass(AST.SeqsoundNode)
def analise(self):
	return self.tok

# AccNode
# 'acc : LPAREN seqnotas RPAREN' | AST.AccNode([p[2]])
@addToClass(AST.AccNode)
def analise(self):
	# PRECISA COLOCAR QUE ESSA SEQ DE NOTAS É ACORDE
	return self

# SeqNotasNode
# 'seqnotas : nota' | AST.SeqNotasNode([p[1]])
# 'seqnotas : nota COMMA seqnotas' | AST.SeqNotasNode([p[1], p[3]])
@addToClass(AST.SeqNotasNode)
def analise(self):
	nota = self.children[0].analise()
	if not (type(nota) is str and findSymbol(nota)):
		return False  # ERRO DE ESCOPO

	ret = [nota]
	if len(self.children) > 1:
		ret = ret + self.children[1]

	return ret

# TokenNode ()
@addToClass(AST.TokenNode)
def analise(self):
	return self.tok

# RepeatNode
# 'loop : REPEAT INT TWOPOINTS NEWLINE program ENDREPEAT' | AST.RepeatNode([AST.TokenNode(p[2]), p[5]])
@addToClass(AST.RepeatNode)
def analise(self):
	return self

## This is the function to execute the semantic analiser
def run(ast):
	ast.analise()
	#print("Semantic Analisys Completed...")
