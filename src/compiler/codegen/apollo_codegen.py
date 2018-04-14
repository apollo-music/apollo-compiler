#AST stuff to use the annotations
from compiler.AST import AST
from compiler.AST.AST import addToClass

AST.blockNb = 0

amp = 100
dur = 200

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
	print("import midi")
	print("pattern = midi.Pattern(format=1, resolution = 100, tick_relative=1)")
	print("track = midi.Track()")
	print("beat = 0")
	print("pattern.append(track)\n")

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
		print(c)	#DEBUG
		c.compile()
	return self

# CommandNode 
# - 'command : command COMMA param' | AST.CommandNode([p[3], p[1]])
# - 'command : PLAY TWOPOINTS LBRACKET expression RBRACKET' | AST.PlayNode([p[4]])
@addToClass(AST.CommandNode)
def compile(self):
	left = self.children[0]
	right = self.children[1]

	amp_before = amp
	dur_before = dur

	left.compile()
	right.compile()

	amp = amp_before
	dur = dur_before

	return self

# ExpressionNode 
# - 'expression : acc' | AST.ExpressionNode([p[1]])
# - 'expression : acc COMMA expression' | AST.ExpressionNode([p[1], p[3]])
@addToClass(AST.ExpressionNode)
def compile(self):
	if len(self.children) == 1:
		return [self.children[0].compile()]
	else:
		return [self.children[0].compile()] + [self.children[1].compile()]

# TokenNode ()
# - 	MULTIPLE USES :S - I'm very confused
@addToClass(AST.TokenNode)
def compile(self):
	print(self.tok)		# DEBUG
	return self.tok

# AmpNode
# - 'param : AMP TWOPOINTS INT' | p[0] = AST.AmpNode([AST.TokenNode(p[3])])
@addToClass(AST.AmpNode)
def compile(self):
	print("amp = " + self.tok)
	amp = self.tok
	return self

# DurNode
# - 'param : DUR TWOPOINTS INT' | p[0] = AST.DurNode([AST.TokenNode(p[3])])
@addToClass(AST.DurNode)
def compile(self):
	print("dur = " + self.tok)
	dur = self.tok
	return self

# VarNode
# 'assignation : VAR ID TWOPOINTS LBRACKET expression RBRACKET' |
# 	 AST.VarNode([AST.TokenNode(p[2]), p[5]])
# 'assignation : VAR ID TWOPOINTS acc' | AST.VarNode([AST.TokenNode(p[2]), p[4]])
@addToClass(AST.VarNode)
def compile(self):
	left = self.children[0]
	right = self.children[1]

	if right.type == "Acc":
		print(str(left.tok) + " = " + str(right.compile()))
	else:
		print(str(left.tok) + " = [" + str(right.compile()) + "]")

	return self

# AccNode
# - 'acc : LPAREN seqnotas RPAREN' | AccNode([p[2]])
# - 'acc : nota' |  AST.AccNode([p[1]])
@addToClass(AST.AccNode)
def compile(self):
	return (self.children[0].compile())


# SeqNotasNode
# 'seqnotas : nota' | AST.SeqNotasNode([p[1]])
# 'seqnotas : nota COMMA seqnotas' | AST.SeqNotasNode([p[1], p[3]])
@addToClass(AST.SeqNotasNode)
def compile(self):
	if len(self.children) == 1:
		return [self.children[0].compile()]
	else:
		return [self.children[0].compile()] + [self.children[1].compile()]

def playNotes(notes):
	for n in notes:
		print("note_on = midi.NoteOnEvent(tick=beat, velocity= " + amp + ", pitch=" + n + ")")
		print("track.append(note_on)")

	print("beat = " + dur)

	for n in notes:
		print("note_off = midi.NoteOnEvent(tick=beat, velocity=0, pitch=" + n + ")")
		print("track.append(note_off)")
		print("beat = 0")

# PlayNode
# 'command : PLAY TWOPOINTS LBRACKET expression RBRACKET' | AST.PlayNode([p[4]])
@addToClass(AST.PlayNode)
def compile(self):
	exp = self.children[0].compile()

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
