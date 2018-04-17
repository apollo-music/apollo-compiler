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
	print("Semantic Analisys Completed...")

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
		if elem in self.symbols:
			return True
		while node.parent:
			if elem in self.symbols:
				return True
			node = node.parent
		return False

	def AddSymbol(self, symbol):
		self.symbols.append(symbol)

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
			if not scopeNode.FindInScope(self.tok):
				raise exceptions.VariableNotDefinedError(self.tok)

@addToClass(AST.AmpNode)
def analise(self, scopeNode):
	for child in self.children:
		child.analise(scopeNode)

@addToClass(AST.DurNode)
def analise(self, scopeNode):
	for child in self.children:
		child.analise(scopeNode)
	
@addToClass(AST.VarNode)
def analise(self, scopeNode):
	left = self.children[0]
	right = self.children[1]

	scopeNode.AddSymbol(left.tok)
	
	if right.type == "Acc":
		right.analise(scopeNode)

@addToClass(AST.AccNode)
def analise(self, scopeNode):
	child = self.children[0]
	child.analise(scopeNode)
	
@addToClass(AST.SeqNotasNode)
def analise(self, scopeNode):
	for child in self.children:
		child.analise(scopeNode)

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
