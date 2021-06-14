class Graph:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
    
    def addEdge(self, src, dst, wt):
        # Source(src) and destination(dst) are the vertices
        # Weight(wt) is the edge that connects the source and destination
        # Graph = [[source, destination, weight], [...]]
        self.graph.append([src, dst, wt])

    def minimumSpanningTree(self, result):
        # Summation of the weights
        total = 0
        for src, dst, wt in result:
            total += wt
         
        return total

    def find(self, parent, key):
        if parent[key] == key:
            return key
        return self.find(parent, parent[key])

    def union(self, parent, rank, x, y):

        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            # When the ranks are equal, it will not matter who'd be pointing to who.
            # It can be parent[x] = y and rank[y] += 1, it doesn't matter.
            # In this case variable x would always be the one to increment.
            parent[y] = x
            rank[x] += 1

    def kruskal(self):
        # Sorts all the edges in non-decreasing order of their weight.
        self.graph = sorted(self.graph, key = lambda item: item[2]) 
        
        # Default initialization
        result = [] # Edges with the shortest weight
        parent = []
        rank = []
        index = 0  # Used for traversing graph

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        # Repeat until there are vertex-1 edges in the resulting spanning tree.
        while len(result) != self.vertices - 1:

            # [source, destination, weight]
            src, dst, wt = self.graph[index]
            index = index + 1

            # Find absolute parent of source and destination
            x = self.find(parent, src)
            y = self.find(parent, dst)

            # If cycle is not formed, include this edge;
            if x != y:
                result.append([src, dst, wt])
                self.union(parent, rank, x, y)
            # Else, discard it.

        print("Minimum Spanning Tree:", self.minimumSpanningTree(result))
        