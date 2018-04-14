import os
import compiler.parser.apollo_yacc as parser
import compiler.lexer.test_lexer as testlexer

#def run_tests():
	#dirs = os.listdir()
	#dirs = ['lexer']
	#for dir in dirs:
		#if os.path.isdir(dir):
	#os.system('python3 compiler/lexer/test_lexer.py')

if __name__ == '__main__':
	testlexer.run()
