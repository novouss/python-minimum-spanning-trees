# Minimum Spanning Tree
A minimum spanning tree or minimum weight spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight. That is, it is a spanning tree whose sum of edge weights is as small as possible.

## Kruskal's Algorithm
Kruskal’s Algorithm builds the spanning tree by adding edges one by one into a growing spanning tree. Kruskal's algorithm follows greedy approach as in each iteration it finds an edge which has least weight and add it to the growing spanning tree.

Algorithm Steps:
<ol>
    <li>Sort all the edges in non-decreasing order of their weight.</li>
    <li>Pick the smallest edge.</li> 
        <ul>
            <li>Check if it forms a cycle with the spanning tree formed so far.</li>
            <li>If cycle is not formed, include the edge. </li>
            <li>Else, discard it. </li>
        </ul>
    <li>Repeat step 2 until there are (V-1) edges in the resulting spanning tree.</li>
</ol>

## Prim's Algorithm
The idea behind Prim’s algorithm is simple, a spanning tree means all vertices must be connected. So the two disjoint subsets (discussed above) of vertices must be connected to make a Spanning Tree. And they must be connected with the minimum weight edge to make it a Minimum Spanning Tree.

Algorithm Steps:
<ol>
    <li>Initialize the minimum spanning tree with a vertex chosen at random.</li>
    <li>Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree</li>
    <li>Keep repeating step 2 until we get a minimum spanning tree</li>
</ol>

# mst.py
```py
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
        result = [] # Edges with the shortes weight
        parent = []
        rank = []
        index = 0  # Used for traversing graph

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        # Repeat unti there are vertex-1 edges in the resulting spanning tree.
        while len(result) != self.vertices - 1:

            #
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
            
```
