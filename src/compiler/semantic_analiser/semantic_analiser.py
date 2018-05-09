import sys
from ..AST import AST
from ..AST.AST import addToClass
from ..AST.AST import Node
from ..exceptions import exceptions


AST.ScopeStack = []

###############
# Op on Stack #
###############
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

###############
# Scope class #
###############
class Scope():
	'''
		The scope class defines a scope holding the value of the variables
		ans which scopes the scope can access
	'''
	name = ""
	dependency = 0
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
	
	def isInScope(self, d):
		self.definitions.get(key, False)


########################
## Analiser Functions ##
########################
# GenericNode
@addToClass(AST.Node)
def analise(self):
	for c in self.children:
		c.analise()
	return self

# EntryNode (First node of program)
# - 'program2 : START NEWLINE program END NEWLINE' | AST.EntryNode(p[3])
@addToClass(AST.EntryNode)
def analise(self):
	return self

# ProgramNode (generic)
# - 'program : statement NEWLINE' | AST.ProgramNode(p[1])
# - 'program : statement NEWLINE program' | AST.ProgramNode([p[1]] + [p[3]])
@addToClass(AST.ProgramNode)
def analise(self):
	for c in self.children:
		# DEBUG print('ProgramNode:\n' + str(c))
		c.analise()
	return self

# CommandNode
# - 'command : command COMMA param' | AST.CommandNode([p[3], p[1]])
# - 'command : PLAY TWOPOINTS LBRACKET expression RBRACKET' | AST.PlayNode([p[4]])
@addToClass(AST.CommandNode)
def analise(self):
	return self

# ExpressionNode
# - 'expression : acc' | AST.ExpressionNode([p[1]])
# - 'expression : acc COMMA expression' | AST.ExpressionNode([p[1], p[3]])
@addToClass(AST.ExpressionNode)
def analise(self):
	return acc

# TokenNode ()
# - 	MULTIPLE USES :S - I'm very confused
@addToClass(AST.TokenNode)
def analise(self):
	return self.tok

# AmpNode
# - 'param : AMP TWOPOINTS INT' | p[0] = AST.AmpNode([AST.TokenNode(p[3])])
@addToClass(AST.AmpNode)
def analise(self):
	return self

# DurNode
# - 'param : DUR TWOPOINTS INT' | p[0] = AST.DurNode([AST.TokenNode(p[3])])
@addToClass(AST.DurNode)
def analise(self):
	return self

# InstrNode
# - 'param : INSTR TWOPOINTS INT' | p[0] = AST.InstNode([AST.TokenNode(p[3])])
@addToClass(AST.InstrNode)
def analise(self):
	return self

# VarNode
# 'assignation : VAR ID TWOPOINTS LBRACKET expression RBRACKET' |
# 	 AST.VarNode([AST.TokenNode(p[2]), p[5]])
# 'assignation : VAR ID TWOPOINTS acc' | AST.VarNode([AST.TokenNode(p[2]), p[4]])
@addToClass(AST.VarNode)
def analise(self):
	return self

# AccNode
# - 'acc : LPAREN seqnotas RPAREN' | AccNode([p[2]])
# - 'acc : nota' |  AST.AccNode([p[1]])
@addToClass(AST.AccNode)
def analise(self):
	# PRECISA COLOCAR QUE ESSA SEQ DE NOTAS É ACORDE
	return self

# RepeatNode
# 'loop : REPEAT INT TWOPOINTS NEWLINE program ENDREPEAT' | p[0] = AST.RepeatNode([AST.TokenNode(p[2]), p[5]])
@addToClass(AST.RepeatNode)
def analise(self):
	return self

# OpNode
# 	| nota : nota SUM nota
#	| nota MINUS nota
#	| nota MULTIPLY nota
# AST.OpNode(p[2], [p[1], p[3]])
@addToClass(AST.OpNode)
def analise(self):
	return self


# SeqNotasNode
# 'seqnotas : nota' | AST.SeqNotasNode([p[1]])
# 'seqnotas : nota COMMA seqnotas' | AST.SeqNotasNode([p[1], p[3]])
@addToClass(AST.SeqNotasNode)
def analise(self):
	# DEBUG print("SeqNotasNodeSeq:\n" + str(self.children))
	# DEBUG print(self.children[0].analise())
	nota = self.children[0].analise()
	return [nota]

# PlayNode
# 'command : PLAY TWOPOINTS LBRACKET expression RBRACKET' | AST.PlayNode([p[4]])
@addToClass(AST.PlayNode)
def analise(self):
	exp = self.children[0].analise()
	playNotes(exp)

## This is the function to execute the semantic analiser
def run(ast):
	# analise(ast, symtable)
	# print("Starting Semantic Analisys ...")
	ast.analise()
	#print("Semantic Analisys Completed...")


# scope = ""
# parent = None
# symbols = []
# def __init__(self, scope, children=None):
# 	self.scope = scope
# 	if not children: self.children = []
# 	elif hasattr(children,'__len__'):
# 		self.children = children
# 	else:
# 		self.children = [children]

# 	for child in self.children:
# 		child.parent = self

# def AddChild(self, child):
# 	self.children.append(child)
# 	child.parent = self

# # Check if element exists in scope
# def FindInScope(self, elem):
# 	node = self
# 	sym = FindSymbol(self.symbols, elem)
# 	if sym != None:
# 		return sym
# 	while node.parent:
# 		sym = FindSymbol(self.symbols, elem)
# 		if sym != None:
# 			return sym
# 		node = node.parent
# 	return None

# # def FindScopeParent(self, scope):
# # 	node = self
# # 	if scope == self.scope:
# # 		return True
# # 	while node.parent:
# # 		if scope == self.scope:
# # 			return True
# # 		node = node.parent
# # 	return False

# def AddSymbol(self, symbol, ASTNode):
# 	self.symbols.append([symbol,ASTNode])


# @addToClass(AST.Node)
# def analise(self, scopeNode):
# 	for child in self.children:
# 		child.analise(scopeNode)

# @addToClass(AST.EntryNode)
# def analise(self, scopeNode):
# 	for child in self.children:
# 		child.analise(scopeNode)

# @addToClass(AST.TokenNode)
# def analise(self, scopeNode):
# 	if isinstance(self.tok, str):
# 			if scopeNode.FindInScope(self.tok) == None:
# 				raise exceptions.VariableNotDefinedError(self.tok)

# @addToClass(AST.AmpNode)
# def analise(self, scopeNode):
# 	for child in self.children:
# 		child.analise(scopeNode)

# @addToClass(AST.DurNode)
# def analise(self, scopeNode):
# 	for child in self.children:
# 		child.analise(scopeNode)

# @addToClass(AST.InstrNode)
# def analise(self, scopeNode):
# 	for child in self.children:
# 		child.analise(scopeNode)

# @addToClass(AST.VarNode)
# def analise(self, scopeNode):
# 	left = self.children[0]
# 	right = self.children[1]

# 	scopeNode.AddSymbol(left.tok, self)

# 	right.analise(scopeNode)

# @addToClass(AST.AccNode)
# def analise(self, scopeNode):
# 	child = self.children[0]
# 	child.analise(scopeNode)

# @addToClass(AST.SeqNotasNode)
# def analise(self, scopeNode):
# 	left = self.children[0]

# 	left.analise(scopeNode)
# 	if left.type == 'Token' and isinstance(left.tok, str):
# 		sym = scopeNode.FindInScope(left.tok)
# 		if sym != None and sym[1].children[1].type == 'Expression':
# 			raise exceptions.SequenceInsideAccError()

# 	if len(self.children)==2:
# 		self.children[1].analise(scopeNode)

# @addToClass(AST.ExpressionNode)
# def analise(self, scopeNode):
# 	for child in self.children:
# 		child.analise(scopeNode)

# @addToClass(AST.CommandNode)
# def analise(self, scopeNode):
# 	for child in self.children:
# 		child.analise(scopeNode)

# @addToClass(AST.PlayNode)
# def analise(self, scopeNode):
# 	for child in self.children:
# 		child.analise(scopeNode)
