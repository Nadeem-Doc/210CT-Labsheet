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
        toVisit = [ self.list[ 0 ] ] 

        while len(toVisit)!= 0:
            currentNode = toVisit.pop()  
            if currentNode not in visited:
                visited.append( currentNode )
                for edge in self.edges[ currentNode ]:
                    if edge != 0:
                        toVisit.append( edge ) 

        return visited

    def travBFS(self):
        toVisit = Queue()   
        visited = []
        toVisit.put( self.list[ 0 ] )

        while toVisit.empty() != True:
            currentNode = toVisit.get()
            
            if currentNode not in visited:
                visited.append( currentNode )

            for edge in self.edges[ currentNode ]:
                if edge not in toVisit.queue:   
                    if edge != 0:
                        toVisit.put( edge )
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
