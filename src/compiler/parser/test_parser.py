from ..parser import apollo_yacc as parser
from ..lexer.apollo_lex import tokens
import unittest
import sys
import os
from ..exceptions import exceptions as exc

datas = []
datas_e = []

n_correct_tests = 2
n_incorrect_tests = 1

dir_path = os.path.dirname(os.path.realpath(__file__))
print (dir_path)

for i in range(n_correct_tests):
    with open(dir_path + '/test_files/test' + str(i+1) + '_parser.apollo', 'r') as myfile:
        datas.append(myfile.read())
        myfile.close()

for i in range(n_incorrect_tests):
    with open(dir_path + '/test_files/test' + str(i+n_correct_tests+1) + '_parser.apollo', 'r') as myfile:
        datas_e.append(myfile.read())
        myfile.close()

class ParserTest(unittest.TestCase):
    def test_parser(self):
        for i in range(len(datas)):
            parser.run(datas[i])

    def test_parser_errors(self):
        for i in range(len(datas_e)):
            parser.run(datas_e[i])
            self.assertRaises(exc.MySyntaxError)

# Tests performed:
# - Test 1: regular program. Should be OK.
# - Test 2: like test 1, with empty spaces added. Should be OK.
# - Test 3: doesn't contain a needed character ']'. Should raise exception MySyntaxError.

def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(ParserTest)
    unittest.TextTestRunner(verbosity=2).run(suite)