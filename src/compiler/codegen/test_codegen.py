from ..codegen import apollo_codegen as codegen
import unittest
import sys
import os
from ..exceptions import exceptions as exc

#datas = []
expected = []
n_tests = 3

dir_path = os.path.dirname(os.path.realpath(__file__))

for i in range(n_tests):
    with open(dir_path + '/__snapshot__/exp_test' + str(i+1) + '_codegen.txt', 'r') as myfile:
        expected.append(myfile.read())
        myfile.close()

class CodeGenTest(unittest.TestCase):
    def test_codegen(self):
        for i in range(n_tests):
            file_path = dir_path + '/test_files/test' + str(i+1) + '_codegen.apollo'
            self.assertEqual(codegen.test(file_path), str(expected[i]))

# Tests performed:
# - Tests 1-3: regular programs. Should be OK.

def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(CodeGenTest)
    unittest.TextTestRunner(verbosity=2).run(suite)