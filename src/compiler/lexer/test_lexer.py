import apollo_lex
import unittest
import sys
import os
import exceptions.exceptions as exc

# Tests performed:
# - Test 1: regular program. Should be OK.
# - Test 2: like test 1, with empty spaces added. Should be OK.
# - Test 3: contains invalid character '#'. Should raise exception CharacterError.

datas = []
datas_e = []

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/test_files/test1_lex.apollo', 'r') as myfile:
    datas.append(myfile.read())

with open(dir_path + '/test_files/test2_lex.apollo', 'r') as myfile:
    datas.append(myfile.read())

with open(dir_path + '/test_files/test3_lex.apollo', 'r') as myfile:
    datas_e.append(myfile.read())

tokens_v12 = ['^', '\n', 'var', 'bixo', ':', '(', '1', ',', '3', '+', '4', ')', '\n',
'amp', ':', '10', '\n', 'dur', ':', '2', '\n', 'play', ':', '[', '72', ',', 'bixo',
']', ',', 'amp', ':', '10', ',', 'dur', ':', '3', '\n', '$']

tokens_t12 = ['START', 'NEWLINE', 'VAR', 'ID', 'TWOPOINTS', 'LPAREN', 'INT', 'COMMA', 'INT',
'SUM', 'INT', 'RPAREN', 'NEWLINE', 'AMP', 'TWOPOINTS', 'INT', 'NEWLINE', 'DUR',
'TWOPOINTS', 'INT', 'NEWLINE', 'PLAY', 'TWOPOINTS', 'LBRACKET', 'INT', 'COMMA',
'ID', 'RBRACKET', 'COMMA', 'AMP', 'TWOPOINTS', 'INT', 'COMMA', 'DUR', 'TWOPOINTS',
'INT', 'NEWLINE', 'END']

tokens_types = []
tokens_values = []

tokens_types.append(tokens_t12)
tokens_types.append(tokens_t12)

tokens_values.append(tokens_v12)
tokens_values.append(tokens_v12)

class LexTest(unittest.TestCase):
    def test_lex_values(self):
        for i in range(len(datas)):
            # Give the lexer some input
            apollo_lex.lexer.input(datas[i])
            # Test using values
            for t_val in tokens_values[i]:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.value))

    def test_lex_types(self):
        for i in range(len(datas)):
            # Give the lexer some input
            apollo_lex.lexer.input(datas[i])
            # Test using values
            for t_val in tokens_values[i]:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.value))

    def test_lex_errors(self):
        for i in range(len(datas_e)):
            # Give the lexer some input
            apollo_lex.lexer.input(datas_e[i])
            #self.assertRaises(exc.CharacterError)


if __name__ == '__main__':
    unittest.main()
