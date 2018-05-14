#!/usr/bin/python3
import compiler.parser.apollo_yacc as parser
<<<<<<< HEAD
import compiler.semantic_analiser.semantic_analiser as sm
#import compiler.codegen.apollo_codegen as codegen
=======
import compiler.codegen.apollo_codegen as codegen
>>>>>>> development

# For parser execuion just uncomment parser.run and execute ./start.py filein
# parser.run()
# For sm execuion just uncomment parser.run and execute ./start.py filein
sm.test()
# For usage of codegen, uncomment codege.run() and execute ./start.py filein
<<<<<<< HEAD
# codegen.run()
=======
codegen.run()
#parser.run()
>>>>>>> development


