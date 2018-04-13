import sys
from ..AST import AST
from ..AST.AST import Node

class PreFunctions():
    def pre_Token(node):
        print("Token: " + str(node.tok))
    def pre_Program(node):
        print("pre Program")
    def pre_Amp(node):
        print("pre Amp")
    def pre_Dur(node):
        print("pre Dur")
    def pre_Command(node):
        print("pre Command")
    def pre_Play(node):
        print("pre Play")
    def pre_Var(node):
        print("pre Var")
    def pre_Expression(node):
        print("pre Expression")
    def pre_Acc(node):
        print("pre Acc")
    def pre_SeqNotas(node):
        print("pre SeqNotas")
    def pre_Op(node):
        print("pre Op")
    def pre_default(node):
        print("pre default")
class PosFunctions():
    def pos_Token(node):
        print("pos Token")
    def pos_Program(node):
        print("pos Program")
    def pos_Amp(node):
        print("pos Amp")
    def pos_Dur(node):
        print("pos Dur")
    def pos_Command(node):
        print("pos Command")
    def pos_Play(node):
        print("pos Play")
    def pos_Var(node):
        print("pos Var")
    def pos_Expression(node):
        print("pos Expression")
    def pos_Acc(node):
        print("pos Acc")
    def pos_SeqNotas(node):
        print("pos SeqNotas")
    def pos_Op(node):
        print("pos Op")
    def pos_default(node):
        print("pos default")

def analise( head: Node ):
    if hasattr(PreFunctions, "pre_" + head.type):
        getattr(PreFunctions, "pre_" + head.type)(head)
    else:
        getattr(PreFunctions, "pre_default")(head)
    for child in head.children:
        analise(child)
    if hasattr(PosFunctions, "pos_" + head.type):
        getattr(PosFunctions, "pos_" + head.type)(head)
    else:
        getattr(PosFunctions, "pos_default")(head)

def run(ast):  
    analise(ast)