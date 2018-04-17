import os
import compiler.lexer.test_lexer as testlexer
import compiler.parser.test_parser as testparser

#def run_tests():
	#dirs = os.listdir()
	#dirs = ['lexer']
	#for dir in dirs:
		#if os.path.isdir(dir):
	#os.system('python3 compiler/lexer/test_lexer.py')

if __name__ == '__main__':
	print("\n----------------------- Testing: Lexer ------------------------------")
	testlexer.run()
	print("\n----------------------- Testing: Parser ------------------------------")
	testparser.run()
