#!/bin/python3
import compiler.parser.apollo_yacc as parser
import compiler.codegen.apollo_codegen as codegen

# For parser execuion just uncomment parser.run and execute ./start.py filein
# parser.run()
# For usage of codegen, uncomment codege.run() and execute ./start.py filein
codegen.run()
#parser.run()


