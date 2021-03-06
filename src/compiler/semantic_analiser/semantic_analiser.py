## Apollo music gen semantic analysiss
# This semantic analysis do:
# - Scope checkin: Variables are declared before using it
#    - Checks variables (changes scope on labels, repeats and plays)
#    - Checks amp, dur and instr
#    - MISSING REPEAT						- TODO
# - Valid var use: Check if a var is used an inalid place
#    - Cannot use ouch = [3,4] e play: [1, (2, ouch), 5]
#    - Valid vars on amp, dur (missing on tone)
# - Operation on right types
#    - Length of types are wrong			- TODO
#    - Types are wrong   					- TODO

import sys
from ..AST import AST
from ..AST.AST import addToClass
from ..AST.AST import Node
from ..exceptions import exceptions as excp
from ..semantic_analiser import call_sync

AST.numberOfTracks = 0

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


# Debug variable and method
def print_warning(s):
	if not AST.debugging:
		print(s)

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

	currentScope = len(AST.ScopeStack) - 1

	while currentScope is not None:
	
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

def addDefaultVal(symbol, value):
	scp = AST.ScopeStack[0]
	scp.addDefiniton(symbol, value)

def checkValues(seq):
	for e in seq:
		if type(e) is list or type(e) is tuple:
			checkValues(e)
		else:
			if(e > 255):
				raise excp.SemanticError("Error: %s causes overflow." % (e))
			elif(e < 0):
				raise excp.SemanticError("Error: %s causes underflow." % (e))


def updateDuration(node):
	for c in node.children:
		node.duration += c.duration

########################
## Analiser Functions ##
########################
# GenericNode - Default
@addToClass(AST.Node)
def analise(self):
	whats_so_ever = [c.analise() for c in self.children]
	updateDuration(self)
	return whats_so_ever

# EntryNode (First node of program)
# 'program2 : START NEWLINE program END NEWLINE' -> AST.EntryNode(p[3])
@addToClass(AST.EntryNode)
def analise(self):
	pushScope(Scope('global'), 0)
	c = self.children[0].analise()
	# Maybe do some analysis on c and check if its ok (True) or not (False)
	return True

@addToClass(AST.SleepNode)
def analise(self):
	duration = self.children[0].analise()
	self.duration = duration

# ProgramNode (generic)
# 'program : statement NEWLINE' -> AST.ProgramNode(p[1])
# 'program : statement NEWLINE program' -> AST.ProgramNode([p[1]] + [p[3]])
# '''statement : command | param | assignation | loop'''
@addToClass(AST.ProgramNode)
def analise(self):
	pushScope(Scope('program_' + str(len(AST.ScopeStack))))
	
	statement = [self.children[0].analise()]
	if len(self.children) > 1:
		program = self.children[1].analise()
		statement = statement + program

	updateDuration(self)
	popScope()
	return statement

# AmpNode
# 'param : AMP TWOPOINTS INT | AMP TWOPOINTS ID ' -> AST.AmpNode([AST.TokenNode(p[3])])
@addToClass(AST.AmpNode)
def analise(self):
	amp = self.children[0].analise()

	if not amp:
		raise excp.SemanticError("Error: %s used but never was defined" % (amp))
	elif type(amp) is int or len(amp) == 1:
		insertSymbol('AMP', amp)
		return amp
	else:
		raise excp.SemanticError("Error: Invalid type used on amp: %s" % (amp))

# DurNode
# 'param : DUR TWOPOINTS INT | DUR TWOPOINTS ID' -> AST.DurNode([AST.TokenNode(p[3])])
@addToClass(AST.DurNode)
def analise(self):
	dur = self.children[0].analise()

	if not dur:
		raise excp.SemanticError("Error: %s used but never was defined" % (dur))
	elif type(dur) is int or len(dur) == 1:
		insertSymbol('DUR', dur)
		return dur
	else:
		raise excp.SemanticError("Error: Invalid type used on dur: %s" % (dur))

# InstrNode
# 'param : INSTR TWOPOINTS INT' -> AST.InstNode([AST.TokenNode(p[3])])
@addToClass(AST.InstrNode)
def analise(self):
	ins = self.children[0].analise()
	insertSymbol('INSTR', ins)
	return ins

# ToneNode
# 'param : TONE TWOPOINTS INT | TONE TWOPOINTS ID' -> AST.ToneNode([AST.TokenNode(p[3])])
@addToClass(AST.ToneNode)
def analise(self):
	tone = self.children[0].analise()
	## Missing decoding ID and valid checking

	insertSymbol('TONE', tone)
	return tone

# CallNode
# 'param : CALL TWOPOINTS ID' -> AST.CallNode([AST.TokenNode(p[3])])
@addToClass(AST.CallNode)
def analise(self):
	# This will return the name of the call
	call = self.children[0].analise()

	# Now, needs to find the scope on the stack
	var_val = findSymbol(call)
	if not var_val:
		raise excp.SemanticError("Error: %s does not exists in scope" % (call))
	
	## Must check if its a valid call (var_val is a program :-))

	return var_val

# CueNode
# 'param : Cue TWOPOINTS ID' -> AST.CueNode([AST.TokenNode(p[3])])
@addToClass(AST.CueNode)
def analise(self):
	# This will return the name of the cue
	cue = self.children[0].analise()

	# Now, needs to find the scope on the stack
	var_val = findSymbol(cue)
	if not var_val:
		raise excp.SemanticError("Error: %s does not exists in scope" % (cue))
	
	## Must check if its a valid cue (var_val is a program :-))

	return var_val

# CommandNode
# 'command: command COMMA param' -> AST.CommandNode([p[3], p[1]])
@addToClass(AST.CommandNode)
def analise(self):
	pushScope(Scope('comand_' + str(len(AST.ScopeStack))))

	command = [self.children[0].analise()]
	param = self.children[1].analise()
	
	updateDuration(self)
	popScope()

	return command

# PlayNode
# 'command : PLAY TWOPOINTS playcontent' -> AST.PlayNode([p[3]])
@addToClass(AST.PlayNode)
def analise(self):
	# Check if amp, dur, and instruments are declared on the scope
	exists_amp = findSymbol('AMP')
	exists_dur = findSymbol('DUR')
	exists_inst = findSymbol('INSTR')

	if not exists_amp:
		print_warning("Atention, No Amplitute (amp) defined on the scope, using default;")
		addDefaultVal('AMP', 1)
	if not exists_dur:
		print_warning("Atention, No Duration (dur) defined on the scope, using default;")
		addDefaultVal('DUR', 1)
	if not exists_inst:
		print_warning("Atention, No Instrument (instr) defined on the scope, using default;")
		addDefaultVal('INSTR', 1)

	seqsound = self.children[0].analise()

	# get the play duration	
	if type(seqsound) is int:
		l = 1
	else:
		l = len(seqsound)
	self.duration = l * findSymbol('DUR')

	# Check for overflow/underflow
	checkValues([seqsound])

	return seqsound

# PlaycontentNode
# 'playcontent : LBRACKET seqexp RBRACKET' -> AST.PlaycontentNode([p[2]])
# 'playcontent : ID'  -> AST.PlaycontentNode(AST.TokenNode(p[1]))
# 'playcontent : acc' -> AST.PlaycontentNode(p[1])
@addToClass(AST.PlaycontentNode)
def analise(self):
	play_val = self.children[0].analise()

	# Check if its an ID
	if type(play_val) is str:
		var_val = findSymbol(play_val)
		if not var_val:
			raise excp.SemanticError("Error: %s used but never was defined" % (play_val))
		else:
			return var_val
	return play_val

# VarNode
# 'assignation : VAR ID TWOPOINTS exp' -> AST.VarNode([AST.TokenNode(p[2]), p[4]])
@addToClass(AST.VarNode)
def analise(self):
	ID = self.children[0].analise()
	exp = self.children[1].analise()
	insertSymbol(ID, exp)
	return self

# ExpressionNode
# - 'exp : LBRACKET seqsound RBRACKET rec_op' |  AST.ExpressionNode([p[2], p[4]])
# - 'exp : nota rec_op'| AST.ExpressionNode([p[1], p[2]])
# - 'exp : acc rec_op' -> AST.ExpressionNode([p[1], p[2]])
@addToClass(AST.ExpressionNode)
def analise(self):
	left = self.children[0].analise()
	## Checking if nota is a variable
	if type(left) is str:
		var_val = findSymbol(left)
		if not var_val:
			raise excp.SemanticError("Error: %s used but never was defined" % (left))
		else:
			left = var_val

	rec_op = self.children[1].analise()
	if not rec_op:
		return left

	# Split the op
	operator = rec_op[0]
	operand = rec_op[1]

	# Can be three operation:
	if operator == '+':
		# If its a sum, need to check if the types are compatible
		if type(left) == type(operand):
			if type(left) is int:
			# [1 + 3]
				left += operand
				'''
				if (left > 255):
					raise excp.SemanticError("Error: overflow on operation " + str(left) + " + " + str(operand)) 
				elif (left < 0):
					raise excp.SemanticError("Error: underflow on operation " + str(left) + " + " + str(operand)) 
				'''

			elif len(left) != len(operand):
				# [[1] + [3]] or [(1) + (3)]
				raise excp.SemanticError('Error on operation %s. Length are not the same' % (str(left) + ' + ' + str(operand)))
			else:
				# Do the operation
				# for i,e in enumerate(left):
				#print('TODO: Check overflow on %s' % (str(left) + ' + ' + str(operand)))
				#print(len(left))
				new_list = []
				for i in range(len(left)):
					sum = left[i] + operand[i]
					'''
					if sum > 255:
						raise excp.SemanticError("Error: overflow on operation " + str(left[i]) + " + " + str(operand[i])) 
					if sum < 0:
						raise excp.SemanticError("Error: underflow on operation " + str(left[i]) + " + " + str(operand[i])) 
					'''
					new_list.append(sum)
				if (type(left) == tuple):
					new_list = tuple(new_list)
				left = new_list
		elif type(left) is tuple or type(left) is list and type(operand) is int:
			# This is [1,2] + 3 or (1,2) + 3
			new_l = []
			for e in left:
				new_l.append(e+operand)
			if type(left) is tuple:
				return tuple(new_l)
			else:
				return new_l
		else:
			raise excp.SemanticError('Error on operation %s' % (str(left) + ' + ' + str(operand)))
		return left
	elif operator == '-':
		# If its a minus, need to check if the types are compatible
		if type(left) == type(operand):
			if type(left) is int:
				# [1 + 3]
				left -= operand
				'''
				if (left > 255):
					raise excp.SemanticError("Error: overflow on operation " + str(left) + " + " + str(operand)) 
				elif (left < 0):
					raise excp.SemanticError("Error: underflow on operation " + str(left) + " + " + str(operand)) 
				'''
			elif len(left) != len(operand):
				# [[1] + [3]] or [(1) + (3)]
				raise excp.SemanticError('Error on operation %s. Length are not the same' % (
					str(left) + ' - ' + str(operand)))
			else:
				# Do the operation
				# for i,e in enumerate(left):
				#print('TODO: Check overflow on %s' % (str(left) + ' - ' + str(operand)))
				new_list = []
				for i in range(len(left)):
					sum = left[i] + operand[i]
					'''
					if sum > 255:
						raise excp.SemanticError("Error: overflow on operation " + str(left[i]) + " - " + str(operand[i])) 
					if sum < 0:
						raise excp.SemanticError("Error: underflow on operation " + str(left[i]) + " - " + str(operand[i])) 
					'''
					new_list.append(sum)
				if (type(left) == tuple):
					new_list = tuple(new_list)
				left = new_list
		elif type(left) is tuple or type(left) is list and type(operand) is int:
			# This is [1,2] + 3 or (1,2) + 3
			new_l = []
			for e in left:
				new_l.append(e - operand)
			if type(left) is tuple:
				return tuple(new_l)
			else:
				return new_l
		else:
			raise excp.SemanticError('Error on operation %s' % (str(left) + ' - ' + str(operand)))
		return left
	elif operator == '&':
		if type(operand) is list and type(left) is list:
			# [1,2] & [3,4]
			return left + operand
		elif type(operand) is tuple and type(left) is tuple:
			# (1,2) & (1,2)
			return tuple(list(operand) + list(left))
		elif type(operand) is tuple and type(left) is list:
			# [1,2] & (3, 4)
			raise excp.SemanticError('Error on operation %s. Invalid type' % (str(left) + ' & ' + str(operand)))
		elif type(operand) is list and type(left) is tuple:
			# (1,2) & [3, 4]
			raise excp.SemanticError('Error on operation %s. Invalid type' % (str(left) + ' & ' + str(operand)))
		else:
		 	raise excp.SemanticError('Error1 on operation %s. Invalid type' % (str(left) + ' & ' + str(operand)))
	return left

# SeqexpNode
# 'seqexp : exp COMMA seqexp' -> AST.SeqexpNode([p[1], p[3]])
# 'seqexp : exp' -> AST.SeqexpNode(p[1])
@addToClass(AST.SeqexpNode)
def analise(self):
	### THIS MAY NOT BE WORKING
	exp = self.children[0].analise()
	if len(self.children) > 1:
		segexp = self.children[1].analise()
		if type(exp) is not list:
			exp = [exp]
		if type(segexp) is not list:
			segexp = [segexp]
		return exp + segexp

	return exp

# OpNode
# 'rec_op : SUM exp' ->  AST.OpNode(p[1], [p[2]])
# 'rec_op : MINUS exp' -> AST.OpNode(p[1], [p[2]])
# 'rec_op : AMPERSAND exp' ->  AST.OpNode(p[1], [p[2]])
@addToClass(AST.OpNode)
def analise(self):
	# NEEDS IMPLEMENTATION

	op = self.op
	val = self.children[0].analise()
	return [op, val]

# SeqSoundNode
# 'seqsound : sound COMMA seqsound' -> AST.SeqsoundNode([p[1], p[3]])
# 'seqsound : sound' -> AST.SeqsoundNode(p[1])
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
# 	'''sound : acc | nota''' -> AST.SoundNode(p[1])
@addToClass(AST.SoundNode)
def analise(self):
	acc_or_nota = self.children[0].analise()

	## Checking if nota is a variable
	if type(acc_or_nota) is str:
		var_val = findSymbol(acc_or_nota)
		if not var_val:
			raise excp.SemanticError('Error: %s used but never was defined' %(acc_or_nota))
			# Should break the program? idn
		else:
			return var_val
	
	return acc_or_nota

# AccNode
# 'acc : LPAREN seqnotas RPAREN' -> AST.AccNode([p[2]])
@addToClass(AST.AccNode)
def analise(self):
	seq_notas = self.children[0].analise()

	# Analise seq_notas e ver se tem algum elemtno tipo lista
	# se tiver é por que existe uma variavel tipo [] dento do ()
	for e in seq_notas:
		if type(e) is list:
			raise excp.SemanticError('Error: Invalid type inside a chord\n Check the variable values')

	return tuple(seq_notas)

# SeqNotasNode
# 'seqnotas : nota' -> AST.SeqNotasNode([p[1]])
# 'seqnotas : nota COMMA seqnotas' -> AST.SeqNotasNode([p[1], p[3]])
@addToClass(AST.SeqNotasNode)
def analise(self):
	nota = self.children[0].analise()

	## Checking if nota is a variable
	if type(nota) is str:
		var_val = findSymbol(nota)
		if not var_val:
			raise excp.SemanticError("Error: %s used but never was defined" % (nota))
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
# 'loop : REPEAT INT TWOPOINTS NEWLINE program ENDREPEAT' -> AST.RepeatNode([AST.TokenNode(p[2]), p[5]])
@addToClass(AST.RepeatNode)
def analise(self):
	pushScope(Scope('repeat__' + str(ID)))
	# Gets the number of repretition (Not needed)
	REP = self.children[0].analise()
	# Analise if the program if OK
	program =  self.children[1].analise()
	# Now, remove the scope

	self.duration = REP * self.children[1].duration
	popScope()
	return self


# SequenceNode
# 'sequence : SEQUENCE ID TWOPOINTS NEWLINE program ENDSEQUENCE' -> AST.SequenceNode([AST.TokenNode(p[2]), p[5]])
@addToClass(AST.SequenceNode)
def analise(self):
	# Gets the ID
	ID = self.children[0].analise()
	pushScope(Scope('label__' + str(ID)))
	# Analise if the program if OK
	program =  self.children[1].analise()
	# If it is, add to scope so if the code can find it
	insertSymbol(ID, program)
	updateDuration(self)
	return True

# TrackNode
@addToClass(AST.TrackNode)
def analise(self):
	# Gets the ID
	ID = self.children[0].analise()
	pushScope(Scope('label__' + str(ID)))
	# Analise if the program if OK
	program =  self.children[1].analise()
	# If it is, add to scope so if the code can find it
	insertSymbol(ID, program)

	return True

# EmptyNode
# 'rec_op : ' -> AST.EmptyNode()
@addToClass(AST.EmptyNode)
def analise(self):
	return False


## This is the function to execute the semantic analiser
def run(ast, debugging = False):
	'''
		Execute the semantic analisis on ast argument
	'''
	AST.debugging = debugging
	r = ast.analise()
	call_sync.run(ast)
	return r


def debug(filename=None):
	'''
		This function test the sem analise on the file from argv[1] or from filename (if any)
	'''
	import sys
	import os
	from compiler.parser import apollo_yacc

	if filename is None:
		f = open(sys.argv[1], 'r')
	else:
		f = open(filename, 'r')
	prog = f.read()
	f.close()

	try:
		# Generate ast
		ast = apollo_yacc.parse(prog)
	except:
		print(sys.exc_info()[0])
		print('Failed on AST gen')
		return False

	try:
		# Run semantic analysis
		print('\n' + sys.argv[1] if filename is None else filename)
		run(ast)
		call_sync.run(ast)
	except:
		print(sys.exc_info()[1].msg)
		return False
	

def test(filename=None):
	'''
		This function test the sem analise on the file from argv[1] or from filename (if any)
	'''
	import sys
	import os
	from compiler.parser import apollo_yacc

	if filename is None:
		f = open(sys.argv[1], 'r')
	else:
		f = open(filename, 'r')
	prog = f.read()
	f.close()

	try:
		# Generate ast
		ast = apollo_yacc.parse(prog)
	except:
		print(sys.exc_info()[0])
		print('Failed on AST gen')
		return False

	run(ast, True)
	call_sync.run(ast)
