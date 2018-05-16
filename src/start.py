#!/usr/bin/python3
import compiler.parser.apollo_yacc as parser
import compiler.semantic_analiser.semantic_analiser as sm
import compiler.codegen.apollo_codegen as codegen

# For parser execuion just uncomment parser.run and execute ./start.py filein
# parser.run()
# For sm execuion just uncomment parser.run and execute ./start.py filein
# sm.debug()
# For usage of codegen, uncomment codege.run() and execute ./start.py filein
codegen.run()


