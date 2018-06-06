from ..parser import apollo_yacc as parser
from ..lexer.apollo_lex import tokens
import unittest
import sys
import os
from ..exceptions import exceptions as e

datas = []
expected = []
datas_e = []

n_correct_tests = 3
n_incorrect_tests = 0

dir_path = os.path.dirname(os.path.realpath(__file__))

TESTS_PATH = dir_path + '/../../tests/'

# for i in range(n_correct_tests):
#     with open(dir_path + '/test_files/test' + str(i + 1) + '_parser.apollo', 'r') as myfile:
#         datas.append(myfile.read())
#         myfile.close()
#     with open(dir_path + '/__snapshot__/exp_test' + str(i + 1) + '_parser.txt', 'r') as myfile:
#         expected.append(myfile.read())
#         myfile.close()

class ParserTest(unittest.TestCase):
    def test_test1_parser(self):
        self.maxDiff = None
        # REDO THIS TO PARSER TO OPEN THE FILE PLX
        file = ''
        with open(TESTS_PATH + 'test1_parser.apollo', 'r') as myfile:
            file = myfile.read()
        snapshot = ''
        with open(dir_path + '/__snapshot__/exp_test1_parser.txt', 'r') as myfile:
            snapshot = myfile.read()

        output_parser = str(parser.test(file))
        self.assertEqual(output_parser, str(snapshot))


    def test_test2_parser(self):
        self.maxDiff = None
        # REDO THIS TO PARSER TO OPEN THE FILE PLX
        file = ''
        with open(TESTS_PATH + 'test2_parser.apollo', 'r') as myfile:
            file = myfile.read()
        snapshot = ''
        with open(dir_path + '/__snapshot__/exp_test2_parser.txt', 'r') as myfile:
            snapshot = myfile.read()
            
        output_parser = str(parser.test(file))
        self.assertEqual(output_parser, str(snapshot))

    def test_test3_parser(self):
        self.maxDiff = None
        # REDO THIS TO PARSER TO OPEN THE FILE PLX
        file = ''
        with open(TESTS_PATH + 'test3_parser.apollo', 'r') as myfile:
            file = myfile.read()
        snapshot = ''
        with open(dir_path + '/__snapshot__/exp_test3_parser.txt', 'r') as myfile:
            snapshot = myfile.read()
            
        output_parser = str(parser.test(file))
        self.assertEqual(output_parser, str(snapshot))
 
    def test_test4_parser_errors1(self):
        self.maxDiff = None

        file = ''
        with open(TESTS_PATH + 'test4_parser.apollo', 'r') as myfile:
            file = myfile.read()
        
        with self.assertRaises(e.MySyntaxError):
            parser.test(file)

    def test_test5_parser_errors2(self):
        self.maxDiff = None

        file = ''
        with open(TESTS_PATH + 'test5_parser.apollo', 'r') as myfile:
            file = myfile.read()
        
        with self.assertRaises(e.MySyntaxError):
            parser.test(file)

# Tests performed:
# - Test 1: regular program. Should be OK.
# - Test 2: like test 1, with empty spaces added. Should be OK.
# - Test 3: like test 1, with a variable using '[]' instead of '()'. Should be OK.
# - Test 4: uses '[]' inside of a '()'. Should raise exception MySyntaxError.
# - Test 5: doesn't contain a needed character ']'. Should raise exception MySyntaxError.
def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(ParserTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
