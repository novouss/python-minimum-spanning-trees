from mst import Graph

test_1 = Graph(6)
test_1.addEdge(0,1,1)
test_1.addEdge(1,3,1)
test_1.addEdge(2,4,1)
test_1.addEdge(0,2,2)
test_1.addEdge(2,3,2)
test_1.addEdge(3,4,2)
test_1.addEdge(1,2,3)
test_1.addEdge(3,5,4)
test_1.addEdge(1,4,3)
test_1.addEdge(4,5,3)
test_1.kruskal()
