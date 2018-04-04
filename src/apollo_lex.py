# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
import sys
# List of token names.   This is always required
tokens = (
   'INT',
   'PLAY',
   'TWOPOINTS',
   'LBRACKET',
   'RBRACKET',
   'LPAREN',
   'RPAREN',
   'AMP',
   'DUR',
   'COMMA',
   'NEWLINE',
   'START',
   'END'
)

# Regular expression rules for simple tokens
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_PLAY  = r'PLAY | play'
t_AMP  = r'AMP | amp'
t_DUR  = r'DUR | dur'
t_COMMA  = r','
t_TWOPOINTS = r':'
t_START = r'\^'
t_END = r'\$'

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

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# # Test it out
# f = open(sys.argv[1], 'r')
# prog = f.read()
#
# # Give the lexer some input
# lexer.input(prog)
#
# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok)
