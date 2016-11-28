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

    l.nodeEdge(2,1)
    l.nodeEdge(2,5)
    
    l.nodeEdge(3,1)
    l.nodeEdge(3,5)

    l.nodeEdge(4,1)
    l.nodeEdge(4,5)

    l.nodeEdge(5,2)
    l.nodeEdge(5,3)
    l.nodeEdge(5,4)

    print(l.list, ":::::::::", l.edges)
