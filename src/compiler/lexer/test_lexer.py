import apollo_lex
import unittest
import sys

# Tests performed:
# - Test 1: regular program. Should be OK.
# - Test 2: like test 1, with empty spaces added. Should be OK.

datas = []

with open('test_files/test1_lex.apollo', 'r') as myfile:
    datas.append(myfile.read())

with open('test_files/test2_lex.apollo', 'r') as myfile:
    datas.append(myfile.read())

tokens_values = ['^', '\n', 'var', 'bixo', ':', '(', '1', ',', '3', '+', '4', ')', '\n',
'amp', ':', '10', '\n', 'dur', ':', '2', '\n', 'play', ':', '[', '72', ',', 'bixo',
']', ',', 'amp', ':', '10', ',', 'dur', ':', '3', '\n', '$']

tokens_types = ['START', 'NEWLINE', 'VAR', 'ID', 'TWOPOINTS', 'LPAREN', 'INT', 'COMMA', 'INT',
'SUM', 'INT', 'RPAREN', 'NEWLINE', 'AMP', 'TWOPOINTS', 'INT', 'NEWLINE', 'DUR',
'TWOPOINTS', 'INT', 'NEWLINE', 'PLAY', 'TWOPOINTS', 'LBRACKET', 'INT', 'COMMA',
'ID', 'RBRACKET', 'COMMA', 'AMP', 'TWOPOINTS', 'INT', 'COMMA', 'DUR', 'TWOPOINTS',
'INT', 'NEWLINE', 'END']

class LexTest(unittest.TestCase):
    def test_lex_values(self):
        for data in datas:
            # Give the lexer some input
            apollo_lex.lexer.input(data)
            # Test using values
            for t_val in tokens_values:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.value))

    def test_lex_types(self):
        for data in datas:
            apollo_lex.lexer.input(data)
            # Test using token types
            for t_type in tokens_types:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_type, str(tok.type))


if __name__ == '__main__':
    unittest.main()
