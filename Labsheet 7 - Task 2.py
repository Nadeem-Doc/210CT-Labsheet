from queue import *

class Graph():
    def __init__(self):
        self.list = []
        self.edges = {}

    def newNode (self,node):
        self.list.append(node)

    def nodeEdge(self,node,edge):
        if node in self.edges.keys():
            self.edges[node] += [edge] # appends to an existing key
        else:
            self.edges[node] = [edge] #creates a new key


    def travDFS(self):
        visited = []
        stack = [ self.list[ 0 ] ] 

        while len(stack)!= 0:
            node = stack.pop()  
            if node not in visited:
                visited.append( node )
                for edge in self.edges[ node ]:
                    if edge != 0:
                        stack.append( edge ) 

        return visited

    def travBFS(self):
        Q = Queue()   
        visited = []
        Q.put( self.list[ 0 ] )

        while Q.empty() != True:
            node = Q.get()
            
            if node not in visited:
                visited.append( node )

            for edge in self.edges[ node ]:
                if edge not in Q.queue:   
                    if edge != 0:
                        Q.put( edge )
        return visited

if __name__ == '__main__':        
    l = Graph()
    
    l.newNode(1)
    l.newNode(2)
    l.newNode(3)
    l.newNode(4)
    l.newNode(5)

    l.nodeEdge(1,2)
    l.nodeEdge(1,3)
    l.nodeEdge(1,4)

    l.nodeEdge(2,5)
    
    l.nodeEdge(3,5)

    l.nodeEdge(4,5)

    l.nodeEdge(5,0)

    print("DFS: ", l.travDFS(),"BFS: ", l.travBFS())
