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
	print("import midi\n", file=AST.outfile)
	print("pattern = midi.Pattern(format=1, resolution = 100, tick_relative=1)", file=AST.outfile)
	print("track = midi.Track()", file=AST.outfile)
	print("pattern.append(track)\n", file=AST.outfile)

	for c in self.children:
	# DEBUG print(c)
		c.compile()

	print("eot=midi.EndOfTrackEvent(tick=0)\ntrack.append(eot)\n", file=AST.outfile)
	print("midi.write_midifile(\"" + AST.midiName + "\", pattern)", file=AST.outfile)
	return self

# ProgramNode (generic)
# - 'program : statement NEWLINE' | AST.ProgramNode(p[1])
# - 'program : statement NEWLINE program' | AST.ProgramNode([p[1]] + [p[3]])
@addToClass(AST.ProgramNode)
def compile(self):
	for c in self.children:
		# DEBUG print('ProgramNode:\n' + str(c))
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
	# DEBUG print("ExpressionNode:\n", self)
	if len(self.children) == 1:
		acc = self.children[0].compile()
		# DEBUG print(acc)
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
	# DEBUG print("TokenNode: " + str(self.tok))
	return self.tok

# AmpNode
# - 'param : AMP TWOPOINTS INT' | p[0] = AST.AmpNode([AST.TokenNode(p[3])])
@addToClass(AST.AmpNode)
def compile(self):
	# DEBUG print('AmpNode:\n' +  str(self))
	if len(self.children) == 1:
		amp = self.children[0]
		AST.amp = int(str(amp))
	return self

# DurNode
# - 'param : DUR TWOPOINTS INT' | p[0] = AST.DurNode([AST.TokenNode(p[3])])
@addToClass(AST.DurNode)
def compile(self):
	# DEBUG print('DurNode:\n' + str(self))
	if len(self.children) == 1:
		dur = self.children[0]
		AST.dur = int(str(dur))
	return self

# InstrNode
# - 'param : INSTR TWOPOINTS INT' | p[0] = AST.InstNode([AST.TokenNode(p[3])])
@addToClass(AST.InstrNode)
def compile(self):
	# DEBUG print('InstrNode:\n' + str(self.children[0]))
	if len(self.children) == 1:
		instrCode = self.children[0]
		print("track.append(midi.ProgramChangeEvent(tick=0, channel=0, data=[" + str(instrCode) + "]))\n", file=AST.outfile)

	return self

# VarNode
# 'assignation : VAR ID TWOPOINTS LBRACKET expression RBRACKET' |
# 	 AST.VarNode([AST.TokenNode(p[2]), p[5]])
# 'assignation : VAR ID TWOPOINTS acc' | AST.VarNode([AST.TokenNode(p[2]), p[4]])
@addToClass(AST.VarNode)
def compile(self):
	# DEBUG print("VarNode:\n" + str(self.children))
	left = self.children[0]
	right = self.children[1]

	if right.type == "Acc":
		acc = right.compile()
		# print(str(left.tok) + " = " + str(tuple(acc)), file=AST.outfile)
		if type(acc) is int:
			AST.table[left.tok] = acc
		else:
			AST.table[left.tok] = tuple(acc)
	else:
		expr = right.compile()
		# print(str(left.tok) + " = " + str(expr), file=AST.outfile)
		if type(expr) is int:
			AST.table[left.tok] = expr
		else:
			AST.table[left.tok] = list(expr)

	return self

# AccNode
# - 'acc : LPAREN seqnotas RPAREN' | AccNode([p[2]])
# - 'acc : nota' |  AST.AccNode([p[1]])
@addToClass(AST.AccNode)
def compile(self):
	# PRECISA COLOCAR QUE ESSA SEQ DE NOTAS É ACORDE
	uniq_or_seq = self.children[0].compile()
	# DEBUG print("AccNode2:\n" + str(uniq_or_seq))

	if type(uniq_or_seq) is str:
		return (AST.table).get(uniq_or_seq, "()")
	
	if self.children[0].type == "SeqNotas":
		return tuple(uniq_or_seq)
	else:
		return uniq_or_seq


# OpNode
# 	| nota : nota SUM nota 
#	| nota MINUS nota 
#	| nota MULTIPLY nota
# AST.OpNode(p[2], [p[1], p[3]])
@addToClass(AST.OpNode)
def compile(self):
	op = self.op
	operand1 = self.children[0]
	operand2 = self.children[1]

	operand1 = operand1.compile()
	operand2 = operand2.compile()

	if op == '+':
		return operand1 + operand2

	if op == '-':
		return operand1 - operand2
	
	if op == '*':
		return operand1 * operand2

	return self


# SeqNotasNode
# 'seqnotas : nota' | AST.SeqNotasNode([p[1]])
# 'seqnotas : nota COMMA seqnotas' | AST.SeqNotasNode([p[1], p[3]])
@addToClass(AST.SeqNotasNode)
def compile(self):
	# DEBUG print("SeqNotasNodeSeq:\n" + str(self.children))
	# DEBUG print(self.children[0].compile())
	nota = self.children[0].compile()
	
	if type(nota) is str:
		nota = AST.table.get(nota, ())
		
	if len(self.children) == 1:
		# DEBUG print(nota)
		return [nota]
	else:
		nota = [nota]
		seqnotas = self.children[1].compile()
		nota = nota + seqnotas
		return (nota)


def playNotes(notes):
	def playNotesTuple(acchord):
		for note in acchord:
			print("note_on = midi.NoteOnEvent(tick=0, velocity= " +
				  str(AST.amp) + ", pitch=" + str(note) + ")", file=AST.outfile)
			print("track.append(note_on)", file=AST.outfile)

		print("", file=AST.outfile)
		for i, note in enumerate(acchord):
			if i == 0:
				print("note_off = midi.NoteOnEvent(tick=" + str(AST.dur) + ", velocity=0, pitch=" +
						str(note) + ")", file=AST.outfile)
			else:
				print("note_off = midi.NoteOnEvent(tick=0, velocity=0, pitch=" +
						str(note) + ")", file=AST.outfile)
			print("track.append(note_off)", file=AST.outfile)
		print("", file=AST.outfile)


	if type(notes) is int:
		print("note_on = midi.NoteOnEvent(tick=0, velocity= " + str(AST.amp) + ", pitch=" + str(notes) + ")", file=AST.outfile)
		print("track.append(note_on)", file=AST.outfile)
		print("note_off = midi.NoteOnEvent(tick=" + str(AST.dur) + ", velocity=0, pitch=" + str(notes) + ")", file = AST.outfile)
		print("track.append(note_off)\n", file=AST.outfile)
	elif type(notes) is tuple:
		# It would be better to achieve this perfection with 
		playNotesTuple(notes)
	elif type(notes) is list:
		for note in notes:
			playNotes(note)
	else:
		print("ERROR", str(notes), str(type(notes)))

# PlayNode
# 'command : PLAY TWOPOINTS LBRACKET expression RBRACKET' | AST.PlayNode([p[4]])
@addToClass(AST.PlayNode)
def compile(self):
  	# DEBUG	print('PlayNode:\n' + str(self))
	# DEBUG print(str(self.children))
	exp = self.children[0].compile()
	# DEBUG print('exp:\n' + str(exp))
	playNotes(exp)


def test(file_path):
	from compiler.parser import apollo_yacc
	from compiler.semantic_analiser import semantic_analiser
	import sys, os
	
	f = open(file_path, 'r')
	prog = f.read()
	f.close()

	AST.midiName = "testing"
	AST.outfile = open(file_path + '_intermediate.py', 'w')

	try:
		# Generate ast
		ast = apollo_yacc.parse(prog)
	except:
		print(sys.exc_info()[0])
	
	try:
		# Run semantic analysis
		semantic_analiser.run(ast)
	except:
		print(sys.exc_info()[0])
	
	try:
		# Generate code (analrapist)
		ast.compile()
		AST.outfile.close()
		with open(file_path + '_intermediate.py', 'r') as myfile:
			outputString = myfile.read()
			myfile.close()
		return outputString

	except:
		print(sys.exc_info()[0])

def run():
	from compiler.parser import apollo_yacc
	from compiler.semantic_analiser import semantic_analiser
	import sys, os

	f = open(sys.argv[1], 'r')
	prog = f.read()
	f.close()

	AST.midiName = '.'.join(sys.argv[1].split('.')[:-1]) + ".mid"

	try:
		# Generate ast
		ast = apollo_yacc.parse(prog)
	except:
		print(sys.exc_info()[0])
	
	try:
		# Run semantic analysis
		semantic_analiser.run(ast)
	except:
		print(sys.exc_info()[0])
	
	try:
		# Generate code (analrapist)
		ast.compile()
		AST.outfile.close()
		print("New intermediate generated %s" % AST.midiName)
	except:
		print(sys.exc_info()[0])

	
