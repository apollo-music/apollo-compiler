from ..parser import apollo_yacc as parser
from ..lexer.apollo_lex import tokens
import unittest
import sys
import os
from ..exceptions import exceptions as exc

datas = []
expected = []
datas_e = []

n_correct_tests = 3
n_incorrect_tests = 0

dir_path = os.path.dirname(os.path.realpath(__file__))
for i in range(n_correct_tests):
    with open(dir_path + '/test_files/test' + str(i+1) + '_parser.apollo', 'r') as myfile:
        datas.append(myfile.read())
        myfile.close()
    with open(dir_path + '/__snapshot__/exp_test' + str(i+1) + '_parser.txt', 'r') as myfile:
        expected.append(myfile.read())
        myfile.close()

for i in range(n_incorrect_tests):
    with open(dir_path + '/test_files/test' + str(i+n_correct_tests+1) + '_parser.apollo', 'r') as myfile:
        datas_e.append(myfile.read())
        myfile.close()

class ParserTest(unittest.TestCase):
    def test_parser(self):
        for i in range(len(datas)):
            self.assertEqual(str(parser.parse(datas[i])), str(expected[i]))

    def test_parser_errors(self):
        for i in range(len(datas_e)):
            parser.parse(datas_e[i])
            self.assertRaises(exc.MySyntaxError)

# Tests performed:
# - Test 1: regular program. Should be OK.
# - Test 2: like test 1, with empty spaces added. Should be OK.
# - Test 3: like test 1, with a variable using '[]' instead of '()'. Should be OK.
# - Test 4: uses '[]' inside of a '()'. Should raise exception MySyntaxError.
# - Test 5: doesn't contain a needed character ']'. Should raise exception MySyntaxError.

def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(ParserTest)
    unittest.TextTestRunner(verbosity=2).run(suite)