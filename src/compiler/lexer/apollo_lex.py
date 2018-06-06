# ------------------------------------------------------------
# apollo_lex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
from ply import lex
import sys
from ..exceptions import exceptions as exc
from ..lexer import instruments
from .. lexer import notes

# List of token names. This is always required
tokens = [
   'INT',
   'PLAY',
   'TWOPOINTS',
   'EQUAL',
   'LBRACKET',
   'RBRACKET',
   'LPAREN',
   'RPAREN',
   'AMP',
   'DUR',
   'INSTR',
   'REPEAT',
   'ENDREPEAT',
   'COMMA',
   'NEWLINE',
   'START',
   'END',
   'VAR',
   'ID',
   'SUM',
   'MINUS',
   'MULTIPLY',
   'TONE',
   'AMPERSAND',
   'SEQUENCE',
   'ENDSEQUENCE',
   'CALL',
   'SYNC',
   'CUE',
   'TRACK',
   'ENDTRACK'
]

# Regular expression rules for simple tokens
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_COMMA  = r','
t_TWOPOINTS = r':'
t_EQUAL = r'='
t_START = r'\^'
t_END = r'\$[\n ]*'

t_AMPERSAND = r'\&'
t_SUM = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'

# Define a rule so we can track line numbers
def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	return t

# A regular expression rule with some action code
def t_INT(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_AMP(t):
	r'AMP | amp'
	return t

def t_DUR(t):
	r'DUR | dur'
	return t

def t_VAR(t):
	r'VAR | var'
	return t

def t_PLAY(t):
	r'PLAY | play'
	return t

def t_INSTR(t):
	r'INSTR | instr'
	return t

def t_TONE(t):
	r'TONE | tone'
	return t

def t_CALL(t):
	r'CALL | call'
	return t

def t_REPEAT(t):
	r'REPEAT | repeat'
	return t

def t_ENDREPEAT(t):
	r'ENDREPEAT | endrepeat'
	return t

def t_SEQUENCE(t):
	r'SEQUENCE | sequence'
	return t

def t_ENDSEQUENCE(t):
	r'ENDSEQUENCE | endsequence'
	return t

def t_SYNC(t):
	r'SYNC | sync'
	return t

def t_CUE(t):
	r'CUE | cue'
	return t

def t_TRACK(t):
	r'TRACK | track'
	return t

def t_ENDTRACK(t):
	r'ENDTRACK | endtrack'
	return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'

	if t.value in instruments.instr2int.keys():
		t.type = 'INT'
		t.value = instruments.instr2int[t.value]
	if t.value in notes.note2int.keys():
		t.type = 'INT'
		t.value = notes.note2int[t.value]

	return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
	print("Illegal character '%s' in line '%s'" % (t.value[0], t.lineno))
	t.lexer.skip(1)
	raise exc.CharacterError("In line '%s': '%s' is not a valid Character for Apollo" % (t.lineno, t.value[0]))

# Build the lexer
lexer = lex.lex()


"""
# Test it out
f = open(sys.argv[1], 'r')
prog = f.read()

# Give the lexer some input
lexer.input(prog)

#Tokenize
while True:
	tok = lexer.token()
	
	if not tok:
		break      # No more input
	
	print(tok)
"""
