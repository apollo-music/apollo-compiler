#AST stuff to use the annotations
from compiler.AST import AST
from compiler.AST.AST import addToClass

AST.amp = 100
AST.dur = 200
AST.table = {}
AST.outfile = open('intermediate.py', 'w')
	

# GenericNode
@addToClass(AST.Node)
def compile(self):
	for c in self.children:
		c.compile()
	return self

# EntryNode (First node of program)
# - 'program2 : START NEWLINE program END NEWLINE' | AST.EntryNode(p[3])
@addToClass(AST.EntryNode)
def compile(self):
	print("import midi", file=AST.outfile)
	print("pattern = midi.Pattern(format=1, resolution = 100, tick_relative=1)", file=AST.outfile)
	print("track = midi.Track()", file=AST.outfile)
	print("beat = 0", file=AST.outfile)
	print("pattern.append(track)\n", file=AST.outfile)

	for c in self.children:
		print(c)  # DEBUG
		c.compile()
	return self

# ProgramNode (generic)
# - 'program : statement NEWLINE' | AST.ProgramNode(p[1])
# - 'program : statement NEWLINE program' | AST.ProgramNode([p[1]] + [p[3]])
@addToClass(AST.ProgramNode)
def compile(self):
	for c in self.children:
		print('ProgramNode:\n' + str(c))	#DEBUG
		c.compile()
	return self

# CommandNode 
# - 'command : command COMMA param' | AST.CommandNode([p[3], p[1]])
# - 'command : PLAY TWOPOINTS LBRACKET expression RBRACKET' | AST.PlayNode([p[4]])
@addToClass(AST.CommandNode)
def compile(self):
	left = self.children[0]
	right = self.children[1]

	amp_before = AST.amp
	dur_before = AST.dur

	left.compile()
	right.compile()

	AST.amp = amp_before
	AST.dur = dur_before

	return self

# ExpressionNode 
# - 'expression : acc' | AST.ExpressionNode([p[1]])
# - 'expression : acc COMMA expression' | AST.ExpressionNode([p[1], p[3]])
@addToClass(AST.ExpressionNode)
def compile(self):
	print("ExpressionNode:\n", self)		# DEBUG
	if len(self.children) == 1:
		acc = self.children[0].compile()
		print(acc)							# DEBUG
		return acc
	else:
		acc = self.children[0].compile()
		expr = self.children[1].compile()
		if type(acc) is not list:
			acc = [acc]
		if type(expr) is list:
			acc = acc + expr
		else:
			acc.append(expr)
		return acc

# TokenNode ()
# - 	MULTIPLE USES :S - I'm very confused
@addToClass(AST.TokenNode)
def compile(self):
	print("TokenNode: " + str(self.tok))		# DEBUG
	return self.tok

# AmpNode
# - 'param : AMP TWOPOINTS INT' | p[0] = AST.AmpNode([AST.TokenNode(p[3])])
@addToClass(AST.AmpNode)
def compile(self):
	print('AmpNode:\n' +  str(self))	# DEBUG
	if len(self.children) == 1:
		amp = self.children[0]
		print("amp = " + str(amp), file=AST.outfile)
		AST.amp = int(str(amp))
	return self

# DurNode
# - 'param : DUR TWOPOINTS INT' | p[0] = AST.DurNode([AST.TokenNode(p[3])])
@addToClass(AST.DurNode)
def compile(self):
	print('DurNode:\n' + str(self))  # DEBUG
	if len(self.children) == 1:
		dur = self.children[0]
		print("dur = " + str(dur), file=AST.outfile)
		AST.dur = int(str(dur))
	return self

# VarNode
# 'assignation : VAR ID TWOPOINTS LBRACKET expression RBRACKET' |
# 	 AST.VarNode([AST.TokenNode(p[2]), p[5]])
# 'assignation : VAR ID TWOPOINTS acc' | AST.VarNode([AST.TokenNode(p[2]), p[4]])
@addToClass(AST.VarNode)
def compile(self):
	print("VarNode:\n" + str(self.children))
	left = self.children[0]
	right = self.children[1]

	if right.type == "Acc":
		acc = right.compile()
		print(str(left.tok) + " = " + str(tuple(acc)), file=AST.outfile)
		AST.table[left.tok] = tuple(acc)
	else:
		expr = right.compile()
		print(str(left.tok) + " = " + str(expr), file=AST.outfile)
		AST.table[left.tok] = list(expr)

	return self

# AccNode
# - 'acc : LPAREN seqnotas RPAREN' | AccNode([p[2]])
# - 'acc : nota' |  AST.AccNode([p[1]])
@addToClass(AST.AccNode)
def compile(self):
	# PRECISA COLOCAR QUE ESSA SEQ DE NOTAS É ACORDE
	uniq_or_seq = self.children[0].compile()
	print("AccNode2:\n" + str(uniq_or_seq))

	if type(uniq_or_seq) is str:
		return (AST.table).get(uniq_or_seq, "()")
	
	if self.children[0].type == "SeqNotas":
		return tuple(uniq_or_seq)
	else:
		return uniq_or_seq


# SeqNotasNode
# 'seqnotas : nota' | AST.SeqNotasNode([p[1]])
# 'seqnotas : nota COMMA seqnotas' | AST.SeqNotasNode([p[1], p[3]])
@addToClass(AST.SeqNotasNode)
def compile(self):
	print("SeqNotasNodeSeq:\n" + str(self.children))
	print(self.children[0].compile())
	if len(self.children) == 1:
		nota = self.children[0].compile()
		print(nota)
		return [nota]
	else:
		nota = [self.children[0].compile()]
		seqnotas = self.children[1].compile()
		nota = nota + seqnotas
		return (nota)


def playNotes(notes):
	if type(notes) is int:
		print("beat = 0", file=AST.outfile)
		print("note_on = midi.NoteOnEvent(tick=beat, velocity= " + str(AST.amp) + ", pitch=" + str(notes) + ")", file=AST.outfile)
		print("track.append(note_on)", file=AST.outfile)
		print("beat = " + str(AST.dur), file=AST.outfile)
		print("note_off = midi.NoteOnEvent(tick=beat, velocity=0, pitch=" + str(notes) + ")", file=AST.outfile)
		print("track.append(note_off)", file=AST.outfile)
	# ELSE?

# PlayNode
# 'command : PLAY TWOPOINTS LBRACKET expression RBRACKET' | AST.PlayNode([p[4]])
@addToClass(AST.PlayNode)
def compile(self):
	print('PlayNode:\n' + str(self))  	# DEBUG
	print(str(self.children))			# DEBUG
	exp = self.children[0].compile()
	print('exp:\n' + str(exp))  		# DEBUG
	for acc in exp:
		playNotes(acc)


def run():
	from compiler.parser import apollo_yacc
	import sys, os

	f = open(sys.argv[1], 'r')
	prog = f.read()
	f.close()

	ast = apollo_yacc.parse(prog)
	print(ast)
	compiled = ast.compile()
