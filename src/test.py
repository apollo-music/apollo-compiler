#!/usr/bin/python3
# Tests
import os
import compiler.lexer.test_lexer as testlexer
import compiler.semantic_analiser.test_semantic_analiser as testsem
import compiler.parser.test_parser as testparser
import compiler.codegen.test_codegen as testcodegen


TESTS_PATH = 'tests/'

## MAYBE THIS IDEIA WAS TOO BIG TO DO ON THIS SPRINT - SORRY GUYS
## How tests will be executed
# Tests of codegen will need to be executed:
#  - TEST_LEX will execute lexer only.
#  - TEST_PAR will execute lexer/parser.
#  - SEMAN_AN will execute lexer/parser and then semantic analiser
#  - CODE_GEN will execute the lexer/parser and then semantic analiser and then will codegen
#  - TEST_ALL will execute the lexer/parser, semantic analiser and codegen and will check the output for each one
# The expected_output can be:
#  - OK (If needs to check if return is True)
#  - FALSE (If needs to check if return a False)
#  - ERROR (If needs to check if raises a value)
#  - FILE (Diff the output with a file - the filename will be __<originalname>.snp)
# tests_files =[
# 	{'type': 'SEMAN_AN', 'filename': 'undeclared_var1.apollo', 'expected_output': 'ERROR'},
# 	{'type': 'SEMAN_AN', 'filename': 'undeclared_var2.apollo', 'expected_output': 'ERROR'},
# 	{'type': 'SEMAN_AN', 'filename': 'undeclared_var3.apollo', 'expected_output': 'ERROR'},
# 	{'type': 'SEMAN_AN', 'filename': 'instr_undefined.apollo', 'expected_output': 'ERROR'},
#     {'type': 'SEMAN_AN', 'filename': 'amp_undefined.apollo', 'expected_output': 'ERROR'},
# 	{'type': 'SEMAN_AN', 'filename': 'amp_var_invalid.apollo', 'expected_output': 'ERROR'},
# 	{'type': 'SEMAN_AN', 'filename': 'dur_undefined.apollo', 'expected_output': 'ERROR'},
# 	{'type': 'SEMAN_AN', 'filename': 'dur_var_invalid.apollo', 'expected_output': 'ERROR'},
# 	{'type': 'SEMAN_AN', 'filename': 'function_invalid_call.apollo', 'expected_output': 'ERROR'},
# 	{'type': 'SEMAN_AN', 'filename': 'op_seq_sum_invalid_length.apollo', 'expected_output': 'ERROR'},
# 	{'type': 'SEMAN_AN', 'filename': 'op_seq_sum_invalid_type.apollo', 'expected_output': 'ERROR'},

# 	{'type': 'CODE_GEN', 'filename': 'test1_codegen.apollo', 'expected_output': 'OK'},
# 	{'type': 'CODE_GEN', 'filename': 'test2_codegen.apollo', 'expected_output': 'OK'},
# 	{'type': 'CODE_GEN', 'filename': 'test3_codegen.apollo', 'expected_output': 'OK'},

# 	{'type': 'TEST_ALL', 'filename': 'play.apollo', 'expected_output': 'OK'},
# 	{'type': 'TEST_ALL', 'filename': 'sequence.apollo', 'expected_output': 'OK'},
# 	{'type': 'TEST_ALL', 'filename': 'notes.apollo', 'expected_output': 'OK'},
# 	{'type': 'TEST_ALL', 'filename': 'chord.apollo', 'expected_output': 'OK'},
# 	{'type': 'TEST_ALL', 'filename': 'vars.apollo', 'expected_output': 'OK'},
# 	{'type': 'TEST_ALL', 'filename': 'function.apollo', 'expected_output': 'OK'},
# 	{'type': 'TEST_ALL', 'filename': 'amp_var_valid.apollo', 'expected_output': 'OK'},
# 	{'type': 'TEST_ALL', 'filename': 'dur_var_valid.apollo', 'expected_output': 'OK'},
# 	{'type': 'TEST_ALL', 'filename': 'op_unit_sum.apollo', 'expected_output': 'OK'},
# 	{'type': 'TEST_ALL', 'filename': 'op_unit_sum2.apollo', 'expected_output': 'OK'},
# 	{'type': 'TEST_ALL', 'filename': 'op_seq_sum_valid.apollo', 'expected_output': 'OK'},
# 	{'type': 'TEST_ALL', 'filename': 'op_seq_extends_valid.apollo', 'expected_output': 'OK'},
# 	{'type': 'TEST_ALL', 'filename': 'op_unit_minus.apollo', 'expected_output': 'OK'},
# ]
# def test_semantic_analisis(test):
# 	import sys
# 	import os
# 	from compiler.parser import apollo_yacc
# 	from compiler.semantic_analiser import semantic_analiser
# 	# Open the file
# 	f = open(TESTS_PATH + test['filename'], 'r')
# 	prog = f.read()
# 	f.close()
# 	try:
# 		# Generate ast
# 		ast = apollo_yacc.parse(prog)
# 	except:
# 		print(sys.exc_info()[0])
# 	# Generates the AST
# 	return True

if __name__ == '__main__':
	print("\n----------------------- Testing: Lexer -------------------------------")
	# testlexer.run()

	print("\n----------------------- Testing: Parser ------------------------------")
	# testparser.run()

	print("\n----------------------- Testing: Semantic Analisis -------------------")
	testsem.run()
	
	print("\n----------------------- Testing: CodeGen -----------------------------")
	testcodegen.run()