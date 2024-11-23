class Node:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self):
        self.array = []

    def addNode(self, node: Node):
        pass

    def addEdge(self, src: int, dst: int):
        pass

    def checkEdge(self, src: int, dst: int):
        pass

    def printGraph(self):
        pass



if __name__ == "__main__":
    graph = Graph()

    graph.addNode(Node("A"))
    graph.addNode(Node("B"))
    graph.addNode(Node("C"))
    graph.addNode(Node("D"))
    graph.addNode(Node("E"))

    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(1,4)
    graph.addEdge(2, 3)
    graph.addEdge(2, 4)
    graph.addEdge(4,0)
    graph.addEdge(4,2)

    graph.printGraph()
