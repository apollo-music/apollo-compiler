import apollo_lex
import unittest
import sys

# Tests performed:
# - Test 1: regular program, should be OK

with open('test_files/test2_lex.apollo', 'r') as myfile:
    data = myfile.read()

tokens1 = ['^', '\n', 'var', 'bixo', ':', '(', '1', ',', '3', '+', '4', ')', '\n',
'amp', ':', '10', '\n', 'dur', ':', '2', '\n', 'play', ':', '[', '72', ',', 'bixo',
']', ',', 'amp', ':', '10', ',', 'dur', ':', '3', '\n', '$']

class LexTest(unittest.TestCase):
    def test_lex(self):
        # Give the lexer some input
        apollo_lex.lexer.input(data)
        # Tokenize
        for t in tokens1:
            tok = apollo_lex.lexer.token()
            self.assertEqual(t, str(tok.value))


if __name__ == '__main__':
    unittest.main()
