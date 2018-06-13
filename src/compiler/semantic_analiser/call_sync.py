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

# this will initialize all sync pointers to the corresponding track nodes
@addToClass(AST.Node)
def initializeSyncs(self):
    global track_nodes

    #print("walking sync " + str(self.type))
    if self.type == "Track":
        name = self.children[0].analise()
        sync[name] = (0, self)
        track_nodes[name] = self
    elif self.type == "Program" or self.type == "Entry":
        [c.initializeSyncs() for c in self.children]

# this will initialize the calls to the first calls outside a track
@addToClass(AST.Node)
def initializeCalls(self, delay):
    global H

    #print("walking call " + str(self.type))
    if len(self.children) > 0 and self.children[0].type == "Call": #one lookahead
        name = self.children[0].children[0].analise()
        heapq.heappush(H, (delay, name, self))
        return

    elif self.type == "Program" or self.type == "Entry":
        for c in self.children:
            c.initializeCalls(delay)
            delay += c.duration

# walk pointer up to next sync, if no sync is found, return None
@addToClass(AST.Node)
def walkSync(self, first, delay):
    node = None

    #print("walking sync " + str(self.type))
    if not first:
        if len(self.children) > 0 and self.children[0].type == "Sync":
            return (delay, self)
        elif self.type == "Program":
            for c in self.children:
                (t, node) = c.walkSync(False, delay)
                if node != None:
                    delay = t
                    break
                else:
                    delay += c.duration

        return (delay, node)

    elif len(self.children) >= 2:
        return self.children[1].walkSync(False, delay)
    else:
        return (delay, node)

# walk pointer up to next call, if no call is found, return None
@addToClass(AST.Node)
def walkCall(self, first, delay):
    global H
    node = None
    name = ""

    #print("walking call " + str(self.type))
    if not first:
        if len(self.children) > 0 and (self.children[0].type == "Call" or self.children[0].type == "Cue"):
            name = self.children[0].children[0].analise()
            return (delay, name, self)
        elif self.type == "Program" :
            for c in self.children:
                (t, name, node) = c.walkCall(False, delay)
                if node != None:
                    delay = t
                    break
                else:
                    delay += c.duration

        return (delay, name, node)

    elif len(self.children) >= 2:
        return self.children[1].walkCall(False, delay)
    else:
        return (delay, name, node)


def run(root):
    global H

    print("started call sync algorithm")
    # initialization
    root.initializeSyncs()
    root.initializeCalls(0)

    #print("finished initializing")
    #print(H)

    # algorithm main loop
    while(len(H) > 0):
        # get caller with smallest delay
        # print(H)
        (t1, callee, call_node) = heapq.heappop(H)
        #print("pop!")        

        # get corresponding sync
        (t2, sync_node) = sync[callee]

        # this situation should be impossible
        # if(t1 < t2):
        #     print("ERROR: cant call before sync!")

        # set the relative time
        if sync_node.type == "Program":
            AST.delays[sync_node.children[0]] = t1 - t2
            print(str(sync_node.children[0].type) + " delay " + str(AST.delays[sync_node.children[0]]))
        else:
            AST.delays[sync_node] = t1 - t2
            print(str(sync_node.type) + " " + str(sync_node.children[0].tok) + " delay " + str(AST.delays[sync_node]))

        # walk the callee sync pointer to the next sync node and update
        (t2, sync_node) = sync_node.walkSync(True, 0)
        if sync_node == None:
            sync[callee] = (0, track_nodes[callee])
        else:
            sync[callee] = (t2, sync_node)

        # if its a call node, we need to create a new call pointer and walk it
        if len(call_node.children) > 0 and call_node.children[0].type == "Call":
            print("spawning new call pointer and walking")
            name = call_node.children[0].children[0].analise()
            print(name)
            callee_node = track_nodes[name]
            (delay, name, callee_node) = callee_node.walkCall(True, 0)
            print("finished")
            print(H)
            if callee_node != None:
                heapq.heappush(H, (delay, name, callee_node))
            print(H)

        # walk the caller pointer to the next call/cue
        (t1, callee, call_node) = call_node.walkCall(True, 0)

        # if another call was found, push it to the heap
        if call_node != None:
            heapq.heappush(H, (t1, callee, call_node))
        #print(H)

