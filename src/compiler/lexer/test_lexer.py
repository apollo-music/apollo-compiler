from ..lexer import apollo_lex
import unittest
import sys
import os
from ..exceptions import exceptions as exc


datas = []
datas_e = []
tokens_types = []
tokens_values = []

n_correct_tests = 4
n_incorrect_tests = 1

dir_path = os.path.dirname(os.path.realpath(__file__))

for i in range(n_correct_tests):
    with open(dir_path + '/test_files/test' + str(i+1) + '_lex.apollo', 'r') as myfile:
        datas.append(myfile.read())
        myfile.close()

for i in range(n_incorrect_tests):
    with open(dir_path + '/test_files/test' + str(i+n_correct_tests+1) + '_lex.apollo', 'r') as myfile:
        datas_e.append(myfile.read())
        myfile.close()

tokens_v123 = ['^', '\n', 'var', 'bixo', ':', '(', '1', ',', '3', '+', '4', ')', '\n',
'amp', ':', '10', '\n', 'dur', ':', '2', '\n', 'play', ':', '[', '72', ',', 'bixo',
']', ',', 'amp', ':', '10', ',', 'dur', ':', '3', '\n', '$']

tokens_v4 = ['^', '\n', 'var', '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', ':', '(', '1', ',', '3', '+', '4', ')', '\n',
'amp', ':', '10', '\n', 'dur', ':', '2', '\n', 'play', ':', '[', '72', ',', 'bixo',
']', ',', 'amp', ':', '10', ',', 'dur', ':', '3', '\n', '$']

tokens_t1234 = ['START', 'NEWLINE', 'VAR', 'ID', 'TWOPOINTS', 'LPAREN', 'INT', 'COMMA', 'INT',
'SUM', 'INT', 'RPAREN', 'NEWLINE', 'AMP', 'TWOPOINTS', 'INT', 'NEWLINE', 'DUR',
'TWOPOINTS', 'INT', 'NEWLINE', 'PLAY', 'TWOPOINTS', 'LBRACKET', 'INT', 'COMMA',
'ID', 'RBRACKET', 'COMMA', 'AMP', 'TWOPOINTS', 'INT', 'COMMA', 'DUR', 'TWOPOINTS',
'INT', 'NEWLINE', 'END']

for i in range(3):
    tokens_values.append(tokens_v123)
tokens_values.append(tokens_v4)

for i in range(4):
    tokens_types.append(tokens_t1234)

class LexTest(unittest.TestCase):
    def test_lex_values1(self):
        with open(dir_path + '/test_files/test1_lex.apollo', 'r') as myfile:
            datas1 = myfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas1)
            # Test using values
            for t_val in tokens_v123:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.value))
    
    def test_lex_values2(self):
        with open(dir_path + '/test_files/test2_lex.apollo', 'r') as myfile:
            datas2 = myfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas2)
            # Test using values
            for t_val in tokens_v123:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.value))
    
    def test_lex_values3(self):
        with open(dir_path + '/test_files/test3_lex.apollo', 'r') as myfile:
            datas3 = myfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas3)
            # Test using values
            for t_val in tokens_v123:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.value))
    
    def test_lex_values4(self):
        with open(dir_path + '/test_files/test4_lex.apollo', 'r') as myfile:
            datas4 = myfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas4)
            # Test using values
            for t_val in tokens_v4:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.value))

    def test_lex_types1(self):
        with open(dir_path + '/test_files/test1_lex.apollo', 'r') as myfile:
            datas1 = myfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas1)
            # Test using values
            for t_val in tokens_t1234:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.type))
    
    def test_lex_types2(self):
        with open(dir_path + '/test_files/test2_lex.apollo', 'r') as myfile:
            datas2 = myfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas2)
            # Test using values
            for t_val in tokens_t1234:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.type))

    def test_lex_types3(self):
        with open(dir_path + '/test_files/test3_lex.apollo', 'r') as myfile:
            datas3 = myfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas3)
            # Test using values
            for t_val in tokens_t1234:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.type))

    def test_lex_types4(self):
        with open(dir_path + '/test_files/test4_lex.apollo', 'r') as myfile:
            datas4 = myfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas4)
            # Test using values
            for t_val in tokens_t1234:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.type))

    def test_lex_errors(self):
        with open(dir_path + '/test_files/test5_lex.apollo', 'r') as myfile:
            datas5 = myfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas5)
            self.assertRaises(exc.CharacterError)

# Tests performed:
# - Test 1: regular program. Should be OK.
# - Test 2: like test 1, with empty spaces added. Should be OK.
# - Test 3: like test 1, with multiple '\t' added. Should de OK.
# - Test 4: like test 1, with a variable using ALL characters permitted in Apollo. Should be OK.
# - Test 5: contains invalid character '#'. Should raise exception CharacterError.

def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(LexTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
