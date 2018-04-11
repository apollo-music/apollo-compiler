#AST stuff to use the annotations
from ..AST import AST
from ..AST.AST import addToClass

AST.blockNb = 0

amp = 100
dur = 200

@addToClass(AST.Node)
def compile(self):
	for c in self.children:
		c.compile()

	return self

@addToClass(AST.EntryNode)
def compile(self):
	print("import midi")
	print("pattern = midi.Pattern(format=1, resolution = 100, tick_relative=1)")
	print("track = midi.Track()")
	print("beat = 0")
	print("pattern.append(track)\n")
    return self

@addToClass(AST.TokenNode)
def compile(self):
	return self.tok

@addToClass(AST.AmpNode)
def compile(self):
	print("amp = " + self.tok)
	amp = self.tok
	return self

@addToClass(AST.DurNode)
def compile(self):
	print("dur = " + self.tok)
	dur = self.tok
	return self
	
@addToClass(AST.VarNode)
def compile(self):
    left = self.children[0]
    right = self.children[1]
	
	if right.type == "Acc":
		print(str(left.tok) + " = " + str(right.compile()))
	else:
		print(str(left.tok) + " = [" + str(right.compile()) + "]")
		
    return self

@addToClass(AST.AccNode)
def compile(self):
	return (self.children[0].compile())
    
@addToClass(AST.SeqNotasNode)
def compile(self):
	if len(self.children) == 1:
		return [self.children[0].compile()]
	else:
		return [self.children[0].compile()] + [self.children[1].compile()]

@addToClass(AST.ExpressionNode)
def compile(self):
	if len(self.children) == 1:
		return [self.children[0].compile()]
	else:
		return [self.children[0].compile()] + [self.children[1].compile()]
		
@addToClass(AST.CommandNode) 
def compile(self):
    left = self.children[0]
    right = self.children[1]
    
    amp_before = amp
    dur_before = dur
    
    left.compile()
    right.compile()

	amp = amp_before
	dur = dur_before
	
    return self

def playNotes(notes):
	for n in notes:
		print("note_on = midi.NoteOnEvent(tick=beat, velocity= " + amp + ", pitch=" + n + ")")
		print("track.append(note_on)")
	
	print("beat = " + dur)
	
	for n in notes:
		print("note_off = midi.NoteOnEvent(tick=beat, velocity=0, pitch=" + n + ")")
		print("track.append(note_off)")
		print("beat = 0")
	
@addToClass(AST.PlayNode)
def compile(self):
    exp = self.children[0].compile()
    
    for acc in exp:
		playNotes(acc)

if __name__ == "__main__":
    from parser import parse
    import sys, os

    f = open(sys.argv[1], 'r')
    prog = f.read()
    f.close()
 
    ast = parse(prog)
    compiled = ast.compile()
