import sys
from ..AST import AST
from ..AST.AST import addToClass
from ..AST.AST import Node
from ..exceptions import exceptions

def run(ast):
	symtable = SymTable("global")
	# analise(ast, symtable)
	# print("Starting Semantic Analisys ...")
	ast.analise(symtable)
	#print("Semantic Analisys Completed...")

class SymTable():
	scope = ""
	parent = None
	symbols = []
	def __init__(self, scope, children=None):
		self.scope = scope
		if not children: self.children = []
		elif hasattr(children,'__len__'):
			self.children = children
		else:
			self.children = [children]

		for child in self.children:
			child.parent = self
	
	def AddChild(self, child):
		self.children.append(child)
		child.parent = self

	# Check if element exists in scope
	def FindInScope(self, elem):
		node = self
		sym = FindSymbol(self.symbols, elem)
		if sym != None:
			return sym
		while node.parent:
			sym = FindSymbol(self.symbols, elem)
			if sym != None:
				return sym
			node = node.parent
		return None
	
	# def FindScopeParent(self, scope):
	# 	node = self
	# 	if scope == self.scope:
	# 		return True
	# 	while node.parent:
	# 		if scope == self.scope:
	# 			return True
	# 		node = node.parent
	# 	return False

	def AddSymbol(self, symbol, ASTNode):
		self.symbols.append([symbol,ASTNode])

def FindSymbol(symbols, target):
	for sym in symbols:
		if sym[0] == target:
			return sym
	return None

########################
## Analiser Functions ##
########################

@addToClass(AST.Node)
def analise(self, scopeNode):
	for child in self.children:
		child.analise(scopeNode)

@addToClass(AST.EntryNode)
def analise(self, scopeNode):	
	for child in self.children:
		child.analise(scopeNode)

@addToClass(AST.TokenNode)
def analise(self, scopeNode):
	if isinstance(self.tok, str):
			if scopeNode.FindInScope(self.tok) == None:
				raise exceptions.VariableNotDefinedError(self.tok)

@addToClass(AST.AmpNode)
def analise(self, scopeNode):
	for child in self.children:
		child.analise(scopeNode)

@addToClass(AST.DurNode)
def analise(self, scopeNode):
	for child in self.children:
		child.analise(scopeNode)

@addToClass(AST.RepeatNode)
def analise(self, scopeNode):
	for child in self.children:
		child.analise(scopeNode)

@addToClass(AST.InstrNode)
def analise(self, scopeNode):
	for child in self.children:
		child.analise(scopeNode)

@addToClass(AST.VarNode)
def analise(self, scopeNode):
	left = self.children[0]
	right = self.children[1]

	scopeNode.AddSymbol(left.tok, self)
	
	right.analise(scopeNode)

@addToClass(AST.AccNode)
def analise(self, scopeNode):
	child = self.children[0]
	child.analise(scopeNode)
	
@addToClass(AST.SeqNotasNode)
def analise(self, scopeNode):
	left = self.children[0]

	left.analise(scopeNode)
	if left.type == 'Token' and isinstance(left.tok, str):		
		sym = scopeNode.FindInScope(left.tok)
		if sym != None and sym[1].children[1].type == 'Expression':
			raise exceptions.SequenceInsideAccError()

	if len(self.children)==2:
		self.children[1].analise(scopeNode)

@addToClass(AST.ExpressionNode)
def analise(self, scopeNode):
	for child in self.children:
		child.analise(scopeNode)
		
@addToClass(AST.CommandNode) 
def analise(self, scopeNode):
	for child in self.children:
		child.analise(scopeNode)
	
@addToClass(AST.PlayNode)
def analise(self, scopeNode):
	for child in self.children:
		child.analise(scopeNode)
