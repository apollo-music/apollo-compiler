from ..codegen import apollo_codegen as codegen
import unittest
import sys
import os
from ..exceptions import exceptions as exc

expected = []
n_tests = 3

dir_path = os.path.dirname(os.path.realpath(__file__))

TESTS_PATH = dir_path + '/../../tests/'

COMMON_TESTS = [
    'play.apollo',
    'sequence.apollo',
    'notes.apollo',
    'chord.apollo',
    'vars.apollo',
    'function.apollo',
    'amp_var_valid.apollo',
    'dur_var_valid.apollo',
    'op_unit_sum.apollo',
    'op_unit_sum2.apollo',
    'op_seq_sum_valid.apollo',
    'op_seq_extends_valid.apollo',
    'op_unit_minus.apollo',
    'op_seq_minus_valid.apollo',
    'tone.apollo'
]

class CodeGenTest(unittest.TestCase):
    def test_should_compile_common_properly(self):
        for test in COMMON_TESTS:
            sn = codegen.test(TESTS_PATH + test)
            self.assertTrue(sn)

    def test_codegen1(self):
        with open(dir_path + '/__snapshot__/exp_test1_codegen.txt', 'r') as myfile:
            snapshot = myfile.read()
            file_path = dir_path + '/../../tests/test1_codegen.apollo'
            self.assertEqual(codegen.test(file_path), str(snapshot))
    
    def test_codegen2(self):
        with open(dir_path + '/__snapshot__/exp_test2_codegen.txt', 'r') as myfile:
            snapshot = myfile.read()
            file_path = dir_path + '/../../tests/test2_codegen.apollo'
            self.assertEqual(codegen.test(file_path), str(snapshot))
    
    def test_codegen3(self):
        with open(dir_path + '/__snapshot__/exp_test3_codegen.txt', 'r') as myfile:
            snapshot = myfile.read()
            file_path = dir_path + '/../../tests/test3_codegen.apollo'
            self.assertEqual(codegen.test(file_path), str(snapshot))

    

# Tests performed:
# - Tests 1-3: regular programs. Should be OK.

def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(CodeGenTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
