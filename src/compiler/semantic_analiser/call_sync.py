import sys
from ..AST import AST
from ..AST.AST import addToClass
from ..AST.AST import Node
from ..exceptions import exceptions as excp
import heapq

AST.delays = {} # this hash will store the relative delays of each sync
sync = {} # store the collection of sync pointers
track_nodes = {}
H = [] # this heap will help us getting the cue with the smallest time
delay = 0
flag = False

# this will initialize all sync pointers to the corresponding track nodes
@addToClass(AST.Node)
def initializeSyncs(self):
    global track_nodes

    #print("walking sync " + str(self.type))
    if self.type == "Track":
        name = self.children[0].analise()
        sync[name] = (0, self)
        track_nodes[name] = self
    else:
        [c.initializeSyncs() for c in self.children]

# this will initialize the calls to the first calls outside a track
@addToClass(AST.Node)
def initializeCalls(self):
    global delay
    global H

    #print("walking call " + str(self.type))
    if self.type == "Track" or self.type == "Sequence":
        return
    
    elif self.type == "Play":
        delay += self.duration
    
    elif self.type == "Call":
        name = self.children[0].analise()
        heapq.heappush(H, (delay, name, self))
        return
    
    [c.initializeCalls() for c in self.children]

    if self.type == "Play":
        delay -= self.duration

# walk pointer up to next sync, if no sync is found, return None
@addToClass(AST.Node)
def walkSync(self):
    global flag # this flag will just be used to avoid first node
    global delay

    #print("walking sync " + str(self.type))
    if flag:
        if self.type == "Sync":
            return (delay, self)
        else: 
            if self.type == "Play":
                delay += self.duration

    flag = True
    t = 0
    node = None
    for c in self.children:
        (t, node) = c.walkSync()
        if node != None:
            break

    return (t, node)

# walk pointer up to next call, if no call is found, return None
@addToClass(AST.Node)
def walkCall(self):
    global flag # this flag will just be used to avoid first node
    global delay
    global H

    #print("walking call " + str(self.type))
    if flag:
        if self.type == "Call" or self.type == "Cue": # if calling, we need to create a new call pointer
            name = self.children[0].analise()
            return (delay, name, self)
            
        else: 
            if self.type == "Play":
                delay += self.duration

    flag = True
    t = 0
    node = None
    name = ""
    for c in self.children:
        (t, name, node) = c.walkCall()
        if node != None:
            break

    return (t, name, node)

def run(root):
    global delay
    global flag
    print("started call sync algorithm")
    # initialization
    delay = 0
    root.initializeSyncs()
    root.initializeCalls()

    #print("finished initializing")
    print(H)

    # algorithm main loop
    while(len(H) > 0):
        # get caller with smallest delay
        (t1, callee, call_node) = heapq.heappop(H)
        #print("pop!")
        #print(H)

        # get corresponding sync
        (t2, sync_node) = sync[callee]

        # this situation should be impossible
        if(t1 < t2):
            print("ERROR: cant call before sync!")

        # set the relative time
        if sync_node != None:
            AST.delays[sync_node] = t1 - t2
            print(str(sync_node.type) + " delay " + str(AST.delays[sync_node]))

        # walk the callee sync pointer to the next sync node and update
        flag = False
        delay = 0
        (t2, sync_node) = sync_node.walkSync()
        if sync_node == None:
            sync[callee] = (0, track_nodes[callee])
        else:
            sync[callee] = (t2, sync_node)

        # if its a call node, we need to create a new call pointer and walk it
        if call_node.type == "Call":
            #print("spawning new call pointer and walking")
            name = call_node.children[0].analise()
            #print(name)
            callee_node = track_nodes[name]
            flag = False
            delay = 0
            (delay, name, callee_node) = callee_node.walkCall()
            #print("finished")
            if callee_node != None:
                heapq.heappush(H, (delay, name, callee_node))
            #print(H)

        # walk the caller pointer to the next call/cue
        flag = False
        delay = 0
        (t1, callee, call_node) = call_node.walkCall()

        # if another call was found, push it to the heap
        if call_node != None:
            heapq.heappush(H, (t1, callee, call_node))
        #print(H)

