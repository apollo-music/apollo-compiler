from ..AST import AST
from ..AST.AST import Node

def analise( head: Node ):
    print(head.type)
    for child in head.next:
        analise(child)

if __name__ == "__main__":
    node = AST.ProgramNode(Node())
    node.addNext(AST.TokenNode(Node()))
    node.addNext(Node())
    node.addNext(Node())
    analise(node)