from ..lexer import apollo_lex
import unittest
import sys
import os
from ..exceptions import exceptions as exc

dir_path = os.path.dirname(os.path.realpath(__file__))

TESTS_PATH = dir_path + '/../../tests/'

tokens_v123 = ['^', '\n', 'var', 'bixo', '=', '(', '1', ',', '3', '+', '4', ')', '\n',
'amp', '=', '10', '\n', 'dur', '=', '2', '\n', 'play', ':', '[', '72', ',', 'bixo',
']', ',', 'amp', '=', '10', ',', 'dur', '=', '3', '\n', '$']

tokens_v4 = ['^', '\n', 'var', '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', '=', '(', '1', ',', '3', '+', '4', ')', '\n',
'amp', '=', '10', '\n', 'dur', '=', '2', '\n', 'play', ':', '[', '72', ',', 'bixo',
']', ',', 'amp', '=', '10', ',', 'dur', '=', '3', '\n', '$']

tokens_t1234 = ['START', 'NEWLINE', 'VAR', 'ID', 'EQUAL', 'LPAREN', 'INT', 'COMMA', 'INT',
'SUM', 'INT', 'RPAREN', 'NEWLINE', 'AMP', 'EQUAL', 'INT', 'NEWLINE', 'DUR',
'EQUAL', 'INT', 'NEWLINE', 'PLAY', 'TWOPOINTS', 'LBRACKET', 'INT', 'COMMA',
'ID', 'RBRACKET', 'COMMA', 'AMP', 'EQUAL', 'INT', 'COMMA', 'DUR', 'EQUAL',
'INT', 'NEWLINE', 'END']

class LexTest(unittest.TestCase):
    def test_lex_values1(self):
        with open(TESTS_PATH + 'test1_lex.apollo', 'r') as testfile:
            datas1 = testfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas1)
            # Test using values
            for t_val in tokens_v123:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.value))
    
    def test_lex_values2(self):
        with open(TESTS_PATH + 'test2_lex.apollo', 'r') as testfile:
            datas2 = testfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas2)
            # Test using values
            for t_val in tokens_v123:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.value))
    
    def test_lex_values3(self):
        with open(TESTS_PATH + 'test3_lex.apollo', 'r') as testfile:
            datas3 = testfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas3)
            # Test using values
            for t_val in tokens_v123:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.value))
    
    def test_lex_values4(self):
        with open(TESTS_PATH + 'test4_lex.apollo', 'r') as testfile:
            datas4 = testfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas4)
            # Test using values
            for t_val in tokens_v4:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.value))

    def test_lex_types1(self):
        with open(TESTS_PATH + 'test1_lex.apollo', 'r') as testfile:
            datas1 = testfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas1)
            # Test using values
            for t_val in tokens_t1234:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.type))
    
    def test_lex_types2(self):
        with open(TESTS_PATH + 'test2_lex.apollo', 'r') as testfile:
            datas2 = testfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas2)
            # Test using values
            for t_val in tokens_t1234:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.type))

    def test_lex_types3(self):
        with open(TESTS_PATH + 'test3_lex.apollo', 'r') as testfile:
            datas3 = testfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas3)
            # Test using values
            for t_val in tokens_t1234:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.type))

    def test_lex_types4(self):
        with open(TESTS_PATH + 'test4_lex.apollo', 'r') as testfile:
            datas4 = testfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas4)
            # Test using values
            for t_val in tokens_t1234:
                tok = apollo_lex.lexer.token()
                self.assertEqual(t_val, str(tok.type))

    def test_lex_errors(self):
        with open(TESTS_PATH + 'test5_lex.apollo', 'r') as testfile:
            datas5 = testfile.read()
            # Give the lexer some input
            apollo_lex.lexer.input(datas5)
            self.assertRaises(exc.CharacterError)

    def test_tracks_sould_generate_valid_tokens(self):
        with open(TESTS_PATH + 'tracks.apollo', 'r') as testfile:
            file = testfile.read()
            apollo_lex.lexer.input(file)
        # NNEEDS TO SEE WHAT TO CHECK
        # # Give the lexer some input
        # apollo_lex.lexer.input(datas5)
        # self.assertRaises(exc.CharacterError)
    
# Tests performed:
# - Test 1: regular program. Should be OK.
# - Test 2: like test 1, with empty spaces added. Should be OK.
# - Test 3: like test 1, with multiple '\t' added. Should de OK.
# - Test 4: like test 1, with a variable using ALL characters permitted in Apollo. Should be OK.
# - Test 5: contains invalid character '#'. Should raise exception CharacterError.

def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(LexTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
