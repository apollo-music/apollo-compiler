import os
import compiler.lexer.test_lexer as testlexer
import compiler.semantic_analiser.test_semantic_analiser as testsem

if __name__ == '__main__':
	testlexer.run()
	testsem.run()

