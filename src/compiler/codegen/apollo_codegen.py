from compiler.AST import AST
from compiler.AST.AST import addToClass
from compiler.parser import apollo_yacc
from compiler.semantic_analiser import semantic_analiser
import sys, os

debug = True
AST.amp = 100
AST.dur = 200
AST.tone = 0
AST.table = {}
AST.outfile = open('intermediate.py', 'w')

sleepNote = 0

AST.track_dictionary = {'main': {'node':None, 'ticks':0}}
AST.track_stack = [('main', 'track0')]
AST.call_counter = 0

# GenericNode
@addToClass(AST.Node)
def compile(self):
	for c in self.children:
		c.compile()
	return self

@addToClass(AST.TrackNode)
def compile(self):	
	self.children[0].compile()
	name = self.children[0].tok
	AST.track_dictionary[name] = {'node': self, 'ticks':0}

# EntryNode (First node of program)
# - 'program2 : START NEWLINE program END NEWLINE' | AST.EntryNode(p[3])
@addToClass(AST.EntryNode)
def compile(self):
	if debug:
		print("entry node")
	print("import midi\n", file=AST.outfile)
	print("pattern = midi.Pattern(format=1, resolution = 100, tick_relative=1)", file=AST.outfile)
	print("track0 = midi.Track()", file=AST.outfile)
	print("pattern.append(track0)\n", file=AST.outfile)

	for c in self.children:
	# DEBUG print(c)
		c.compile()


	for i in range(AST.call_counter+1):
		print("eot=midi.EndOfTrackEvent(tick=0)\ntrack"+str(i)+".append(eot)\n", file=AST.outfile)
	print("midi.write_midifile(\"" + AST.midiName + "\", pattern)", file=AST.outfile)
	return self

# ProgramNode (generic)
# - 'program : statement NEWLINE' | AST.ProgramNode(p[1])
# - 'program : statement NEWLINE program' | AST.ProgramNode([p[1]] + [p[3]])
@addToClass(AST.ProgramNode)
def compile(self):
	if debug:
		print("ProgramNode")
	for c in self.children:
		c.compile()
	return self

# CommandNode 
# - 'command : command COMMA param' | AST.CommandNode([p[3], p[1]])
# - 'command : PLAY TWOPOINTS playcontent' | AST.PlayNode([p[3]])
@addToClass(AST.CommandNode)
def compile(self):
	if debug:
		print("command")
	left = self.children[0]
	right = self.children[1]

	amp_before = AST.amp
	dur_before = AST.dur

	left.compile()
	right.compile()

	AST.amp = amp_before
	AST.dur = dur_before

	return self

#compute exp1 (op) exp2
def computeExpression(exp1, exp2, op):
	# Exp1 is a list
	if type(exp1) is list:
		result = []
		# If exp2 is a number, we add/subtract it from all values of exp1
		if type(exp2) is int:
			if op == '+':
				for e in exp1:
					result.append(e + exp2)
			elif op == '-':
				for e in exp1:
					result.append(e - exp2)
		# If exp2 is a list, it has the same length of exp1 (semantic analysis)
		# if its a plus/minus operation, so we add/subtract all values 
		# or else we just append them
		else:
			if op == '+':
				for i in range(len(exp1)):
					result.append(exp1[i] + exp2[i])
			elif op == '-':
				for i in range(len(exp1)):
					result.append(exp1[i] - exp2[i])
			else:
				result = exp1
				result.append(exp2)
		
		return result
	# If exp1 is an int, then exp2 is an int, and we just add/subtract them
	elif type(exp1) is int:
		if op == '+':
			result = exp1 + exp2
		elif op == '-':
			result = exp1 - exp2
		
		return result

	# If exp1 is a tuple
	elif type(exp1) is tuple:
		exp1 = list(exp1)
		result = []
		# If exp2 is a number, we add/subtract it from all values of exp1
		if type(exp2) is int:
			if op == '+':
				for e in exp1:
					result.append(e + exp2)
			elif op == '-':
				for e in exp1:
					result.append(e - exp2)

		# If exp2 is a tuple, it has the same length of exp1 (semantic analysis)
		# if its a plus/minus operation, so we add/subtract all values 
		# or else we just append them
		else:
			exp2 = list(exp2)
			if op == '+':
				for i in range(len(exp1)):
					result.append(exp1[i] + exp2[i])
			elif op == '-':
				for i in range(len(exp1)):
					result.append(exp1[i] - exp2[i])
			else:
				result = exp1 + exp2
		
		return tuple(result)

	else:
		raise SystemExit
		
# ExpressionNode 
# - 'exp : LBRACKET seqsound RBRACKET rec_op' | AST.ExpressionNode([p[2],p[4]])
# - 'exp : nota rec_op' | AST.ExpressionNode([p[1], p[2]])
# - 'exp : acc rec_op' | AST.ExpressionNode([p[1]], p[2]])
# In order to execute the operations, we will expand the rec_op in this node
@addToClass(AST.ExpressionNode)
def compile(self):
	if debug:
		print("expression")
	exp1 = self.children[0].compile()
	rec_op = self.children[1]
	if len(rec_op.children) > 0:
		exp2 = rec_op.children[0].compile()
		op = rec_op.op
		return computeExpression(exp1, exp2, op)

	else:
		return exp1

# SeqexpNode
# - 'seqexp : exp COMMA seqexp' | AST.SeqexpNode([p[1], p[3]])
# - 'seqexp : exp' | AST.SeqexpNode(p[1])
@addToClass(AST.SeqexpNode)
def compile(self):
	if debug:
		print("seqexp")
	exp = self.children[0].compile()
		
	if len(self.children) == 1:
		return exp
	else:
		seqexp = self.children[1].compile()
		
		if not (type(exp) is list):
			exp = [exp]
		if not (type(seqexp) is list):
			seqexp = [seqexp]

		return exp + seqexp

# TokenNode ()
# - 	MULTIPLE USES :S - I'm very confused
@addToClass(AST.TokenNode)
def compile(self):
	if debug:
		print("token " + str(self.tok))
	nota = self.tok
	if type(nota) is str:
		nota = AST.table.get(nota, ())
	return nota

# AmpNode
# 'param : AMP TWOPOINTS INT | AMP TWOPOINTS ID ' -> AST.AmpNode([AST.TokenNode(p[3])])
@addToClass(AST.AmpNode)
def compile(self):
	if debug:
		print("amp")
	if len(self.children) == 1:
		amp = self.children[0].compile()
		if type(amp) is str:
			AST.amp = AST.table.get(amp)
		else:
			AST.amp = int(str(amp))
	return self

# DurNode
# 'param : DUR TWOPOINTS INT | DUR TWOPOINTS ID' -> AST.DurNode([AST.TokenNode(p[3])])
@addToClass(AST.DurNode)
def compile(self):
	if debug:
		print("dur")
	if len(self.children) == 1:
		dur = self.children[0].compile()
		if type(dur) is str:
			AST.dur = AST.table.get(dur)
		else:
			AST.dur = int(str(dur))
	return self

# InstrNode
# - 'param : INSTR TWOPOINTS INT' | p[0] = AST.InstNode([AST.TokenNode(p[3])])
@addToClass(AST.InstrNode)
def compile(self):
	if debug:
		print("instr")
	# DEBUG print('InstrNode:\n' + str(self.children[0]))
	if len(self.children) == 1:
		instrCode = self.children[0].compile()
		print("track.append(midi.ProgramChangeEvent(tick=0, channel=0, data=[" + str(instrCode) + "]))\n", file=AST.outfile)

	return self

# ToneNode
# - 'param : TONE TWOPOINTS INT | TONE TWOPOINTS ID' -> AST.ToneNode([AST.TokenNode(p[3])])
@addToClass(AST.ToneNode)
def compile(self):
	if debug:
		print("tone")
	if len(self.children) == 1:
		tone = self.children[0]
		AST.tone = int(str(tone))
	return self

# VarNode
# 'assignation : VAR ID TWOPOINTS exp' -> AST.VarNode([AST.TokenNode(p[2]), p[4]])
@addToClass(AST.VarNode)
def compile(self):
	if debug:
		print("var")
	left = self.children[0]
	right = self.children[1]

	expr = right.compile()
	#DEBUG print("Inserting " + str(expr) + " in " + str(left.tok))
	AST.table[left.tok] = expr

	return self

# AccNode
# - 'acc : LPAREN seqnotas RPAREN' | AccNode([p[2]])
# - 'acc : nota' |  AST.AccNode([p[1]])
@addToClass(AST.AccNode)
def compile(self):
	if debug:
		print("acc")
	# PRECISA COLOCAR QUE ESSA SEQ DE NOTAS É ACORDE
	uniq_or_seq = self.children[0].compile()
	# DEBUG print("AccNode2:\n" + str(uniq_or_seq))

	if type(uniq_or_seq) is str:
		return (AST.table).get(uniq_or_seq, "()")
	
	if self.children[0].type == "SeqNotas":
		return tuple(uniq_or_seq)
	else:
		return uniq_or_seq

# RepeatNode
# 'loop : REPEAT INT TWOPOINTS NEWLINE program ENDREPEAT' | p[0] = AST.RepeatNode([AST.TokenNode(p[2]), p[5]])
@addToClass(AST.RepeatNode)
def compile(self):
	if debug:
		print("repeat")
	num_repeats = self.children[0].compile()
	prog = self.children[1]

	for i in range(num_repeats):
		prog.compile()
	return self

# SeqSoundNode
# 'seqsound : sound COMMA seqsound' | AST.SeqsoundNode([p[1], p[3]])
# 'seqsound : sound' | AST.SeqsoundNode(p[1])
@addToClass(AST.SeqsoundNode)
def compile(self):
	if debug:
		print("seqsound")
	sound = self.children[0].compile()

	if len(self.children) == 1:
		return [sound]
	else:
		sound = [sound]
		seqsound = self.children[1].compile()
		sound = sound + seqsound
		return sound

# SoundNode
# 'sound : acc' | AST.SoundNode(p[1])
# 'sound : nota' | AST.SoundNode(p[1])
@addToClass(AST.SoundNode)
def compile(self):
	if debug:
		print("sound")
	return self.children[0].compile()

# SeqNotasNode
# 'seqnotas : nota' | AST.SeqNotasNode([p[1]])
# 'seqnotas : nota COMMA seqnotas' | AST.SeqNotasNode([p[1], p[3]])
@addToClass(AST.SeqNotasNode)
def compile(self):
	if debug:
		print("seqnotas")
	nota = self.children[0].compile()
		
	if len(self.children) == 1:
		# DEBUG print(nota)
		return [nota]
	else:
		nota = [nota]
		seqnotas = self.children[1].compile()
		nota = nota + seqnotas
		return (nota)

def sleep(delay):
	print("note_on = midi.NoteOnEvent(tick=0, velocity=0" + ", pitch=" + str(sleepNote) + ")", file=AST.outfile)
	print(AST.track_stack[len(AST.track_stack)-1][1] + ".append(note_on)", file=AST.outfile)
	print("note_off = midi.NoteOnEvent(tick=" + str(delay) + ", velocity=0, pitch=" + str(sleepNote) + ")", file = AST.outfile)
	print(AST.track_stack[len(AST.track_stack)-1][1] + ".append(note_off)\n", file=AST.outfile)

	AST.track_dictionary[AST.track_stack[len(AST.track_stack)-1][0]]["ticks"] += delay

def playNotes(notes):
	def playNotesTuple(acchord):
		for note in acchord:
			note += AST.tone
			print("note_on = midi.NoteOnEvent(tick=0, velocity= " +
				  str(AST.amp) + ", pitch=" + str(note) + ")", file=AST.outfile)
			print(AST.track_stack[len(AST.track_stack)-1][1] + ".append(note_on)", file=AST.outfile)

		print("", file=AST.outfile)
		for i, note in enumerate(acchord):
			note += AST.tone
			if i == 0:
				print("note_off = midi.NoteOnEvent(tick=" + str(AST.dur) + ", velocity=0, pitch=" +
						str(note) + ")", file=AST.outfile)
			else:
				print("note_off = midi.NoteOnEvent(tick=0, velocity=0, pitch=" +
						str(note) + ")", file=AST.outfile)
			print(AST.track_stack[len(AST.track_stack)-1][1] + ".append(note_off)", file=AST.outfile)
		print("", file=AST.outfile)

		AST.track_dictionary[AST.track_stack[len(AST.track_stack)-1][0]]["ticks"] += AST.dur


	if type(notes) is int:
		notes += AST.tone
		print("note_on = midi.NoteOnEvent(tick=0, velocity= " + str(AST.amp) + ", pitch=" + str(notes) + ")", file=AST.outfile)
		print(AST.track_stack[len(AST.track_stack)-1][1] + ".append(note_on)", file=AST.outfile)
		print("note_off = midi.NoteOnEvent(tick=" + str(AST.dur) + ", velocity=0, pitch=" + str(notes) + ")", file = AST.outfile)
		print(AST.track_stack[len(AST.track_stack)-1][1] + ".append(note_off)\n", file=AST.outfile)
		AST.track_dictionary[AST.track_stack[len(AST.track_stack)-1][0]]["ticks"] += AST.dur

	elif type(notes) is tuple:
		# It would be better to achieve this perfection with 
		playNotesTuple(notes)
	elif type(notes) is list:
		for note in notes:
			playNotes(note)
	else:
		print("ERROR", str(notes), str(type(notes)))

# SleepNode
@addToClass(AST.SleepNode)
def compile(self):
	if debug:
		print("sleep")
	dur = self.children[0].compile()	
	print(dur)
	sleep(dur)
	return self

# PlayNode
# 'command : PLAY TWOPOINTS LBRACKET expression RBRACKET' | AST.PlayNode([p[4]])
@addToClass(AST.PlayNode)
def compile(self):
	if debug:
		print("play")
	exp = self.children[0].compile()
	# DEBUG print('exp:\n' + str(exp))
	playNotes(exp)

# SequenceNode
# 'sequence : SEQUENCE ID TWOPOINTS NEWLINE program ENDSEQUENCE' | AST.SequenceNode([AST.TokenNode(p[2]), p[5]])
@addToClass(AST.SequenceNode)
def compile(self):
	if debug:
		print("label")
	name = self.children[0].tok
	#print("sequenceName " + str(name))
	AST.table[name] = self.children[1]

# CallNode
# 'param : CALL TWOPOINTS ID' | AST.CallNode(AST.TokenNode(p[3]))
@addToClass(AST.CallNode)
def compile(self):
	if debug:
		print("label")
	name = self.children[0].tok

	if (name in AST.track_dictionary):
		AST.call_counter += 1
		AST.track_stack.append((name, 'track'+str(AST.call_counter)))		
		print(AST.track_stack[len(AST.track_stack)-1][1] + " = midi.Track()", file=AST.outfile)
		print("pattern.append("+AST.track_stack[len(AST.track_stack)-1][1]+")\n", file=AST.outfile)
		print(AST.track_dictionary[name]["node"].children[1])
		AST.track_dictionary[name]["node"].children[1].compile()
		
		AST.track_stack.pop()

	else:
		# code should never get here due to semantic analysis
		if name not in AST.table:
			print("ERROR UNDEFINED SEQUENCE")

		amp_before = AST.amp
		dur_before = AST.dur

		AST.table[name].compile()

		AST.amp = amp_before
		AST.dur = dur_before

# PlayContent
# 'playcontent : LBRACKET seqexp RBRACKET' | AST.PlaycontentNode([p[2]])
# 'playcontent : ID' | AST.PlaycontentNode(AST.TokenNode(p[1]))
# 'playcontent : acc' | AST.PlaycontentNode(p[1])
@addToClass(AST.PlaycontentNode)
def compile(self):
	return self.children[0].compile()

def test(file_path):
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
	f = open(sys.argv[1], 'r')
	prog = f.read()
	f.close()

	AST.midiName = '.'.join(sys.argv[1].split('.')[:-1]) + ".mid"	
	try:
		# Generate ast
		ast = apollo_yacc.parse(prog)
	except:
		print(sys.exc_info()[0])
		print(sys.exc_info()[1])
			
	# try:
	# 	# Run semantic analysis
	# 	semantic_analiser.run(ast)
	# except:
	# 	print(sys.exc_info()[0])
	
	try:
		# Generate code (analrapist)
		ast.compile()
		AST.outfile.close()
		print("New intermediate generated %s" % AST.midiName)
	except:
		print(sys.exc_info()[0])

	
