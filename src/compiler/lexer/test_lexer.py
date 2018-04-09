import apollo_lex
import unittest
import sys

# Tests performed:
# - Test 1: regular program. Should be OK.
# - Test 2: like test 1, with empty spaces added. Should be OK.

with open('test_files/test1_lex.apollo', 'r') as myfile:
    data = myfile.read()

tokens = ['START', 'NEWLINE', 'VAR', 'ID', 'TWOPOINTS', 'LPAREN', 'INT', 'COMMA', 'INT',
'SUM', 'INT', 'RPAREN', 'NEWLINE', 'AMP', 'TWOPOINTS', 'INT', 'NEWLINE', 'DUR',
'TWOPOINTS', 'INT', 'NEWLINE', 'PLAY', 'TWOPOINTS', 'LBRACKET', 'INT', 'COMMA',
'ID', 'RBRACKET', 'COMMA', 'AMP', 'TWOPOINTS', 'INT', 'COMMA', 'DUR', 'TWOPOINTS',
'INT', 'NEWLINE', 'END']

class LexTest(unittest.TestCase):
    def test_lex(self):
        # Give the lexer some input
        apollo_lex.lexer.input(data)
        # Tokenize
        for t in tokens:
            tok = apollo_lex.lexer.token()
            self.assertEqual(t, str(tok.type))


if __name__ == '__main__':
    unittest.main()
