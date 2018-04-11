#AST stuff to use the annotations
from ..AST import AST
from ..AST.AST import addToClass

AST.blockNb = 0

@addToClass(AST.Node)
def compile(self):
    for c in self.children:
        c.compile()
 
    return self

@addToClass(AST.TokenNode)
def compile(self):
    print('PUSH %s' % self.tok)
    return self

@addToClass(AST.VarNode)
def compile(self):
    left = self.children[0]
    right = self.children[1]
	
	print(str(left.tok) + " = " + right.compile())

    return self

@addToClass(AST.AccNode)
def compile(self):
    left = self.children[0]
    right = self.children[1]
	
	print(str(left.tok) + " = " + right.compile())

    return self
    
@addToClass(AST.OpNode)
def compile(self):
    left = self.children[0]
    right = self.children[1]

    left.compile()
    right.compile()
    
    if self.op == '+':
        print('ADD')
    elif self.op == '-':
        print('SUB')
    elif self.op == '/':
        print('DIV')
    elif self.op == '*':
        print('MUL')
    
    return self

@addToClass(AST.WhileNode) 
def compile(self):
    left = self.children[0]
    right = self.children[1]
    AST.blockNb = AST.blockNb + 1

    print('JMP cond%d' % AST.blockNb)
    print('body%d:' % AST.blockNb)
    right.compile()

    print('cond%d:' % AST.blockNb)
    left.compile()
    print('JNZ body%d' % AST.blockNb)    

    return self

@addToClass(AST.PrintNode)
def compile(self):
    self.children[0].compile()
    print('PRINT')    

if __name__ == "__main__":
    from parser import parse
    import sys, os

    f = open(sys.argv[1], 'r')
    prog = f.read()
    f.close()
 
    ast = parse(prog)
    compiled = ast.compile()
