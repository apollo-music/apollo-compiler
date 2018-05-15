import unittest
import os

from ..semantic_analiser import semantic_analiser
from ..AST import AST
from ..AST.AST import Node
from ..exceptions import exceptions as e

dir_path = os.path.dirname(os.path.realpath(__file__))

TESTS_PATH = dir_path + '/../../tests/'

COMMON_TESTS =[
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
    'op_seq_minus_valid.apollo'
]

class SemanticAnaliserTest(unittest.TestCase):
    def test_should_compile_properly(self):
        for test in COMMON_TESTS:
            sn = semantic_analiser.test(TESTS_PATH+test)
            self.assertTrue(sn)

    def test_should_raises_on_undeclared_var1(self):
        with self.assertRaises(e.SemanticError):
	        semantic_analiser.test(TESTS_PATH + 'undeclared_var1.apollo')

    def test_should_raises_on_undeclared_var2(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'undeclared_var2.apollo')

    def test_should_raises_on_undeclared_var3(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'undeclared_var3.apollo')

    def test_should_raises_on_instr_undefined(self):
        sn = semantic_analiser.test(TESTS_PATH + 'instr_undefined.apollo')
        self.assertTrue(sn)

    def test_should_raises_on_amp_undefined(self):
        sn = semantic_analiser.test(TESTS_PATH + 'amp_undefined.apollo')
        self.assertTrue(sn)

    def test_should_raises_on_amp_var_invalid(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'amp_var_invalid.apollo')

    def test_should_raises_on_dur_undefined(self):
        sn = semantic_analiser.test(TESTS_PATH + 'dur_undefined.apollo')
        self.assertTrue(sn)

    def test_should_raises_on_dur_var_invalid(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'dur_var_invalid.apollo')

    def test_should_raises_on_function_invalid_call(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'function_invalid_call.apollo')

    def test_should_raises_on_op_seq_sum_invalid_length(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'op_seq_sum_invalid_length.apollo')

    def test_should_raises_on_op_seq_sum_invalid_type(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'op_seq_sum_invalid_type.apollo')

    def test_should_raises_on_op_seq_extends_invalid1_type(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'op_seq_extends_invalid1.apollo')
    
    def test_should_raises_on_op_seq_extends_invalid2_type(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'op_seq_extends_invalid2.apollo')

    def test_should_raises_on_op_seq_extends_invalid3_type(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'op_seq_extends_invalid3.apollo')

    def test_should_raises_on_op_seq_extends_invalid4_type(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'op_seq_extends_invalid4.apollo')
    
    def test_should_raises_on_op_seq_minus_invalid_length_type(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'op_seq_minus_invalid_length.apollo')

    def test_should_raises_on_op_seq_minus_invalid_type(self):
        with self.assertRaises(e.SemanticError):
            semantic_analiser.test(TESTS_PATH + 'op_seq_minus_invalid_type.apollo')


def run():
    suite = unittest.TestLoader().loadTestsFromTestCase(SemanticAnaliserTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
