from Graphs.GraphQueue import GraphQueue

"""
Class which contains methods:- BFS(Breadth First Search) and DFS(Depth First Search)
in order to traverse a graph 
"""


class GraphTraversal:

    def bfs(self, adjacency_list):
        print("Breadth First Search\n")
        visited_list = []
        queue = GraphQueue()

        for i in adjacency_list:
            current_node = i

            while current_node is not None:
                if int(current_node.value) not in visited_list:
                    queue.enqueue(current_node)
                    visited_list.append(int(current_node.value))
                current_node = current_node.next

        while not queue.isEmpty():
            current_node = queue.dequeue()
            print(current_node.value)

    def dfs(self, adjaceny_list):
        print("Depth First Search\n")
        visited_list = []
        stack = []

        for i in adjaceny_list:
            current_node = i

            while current_node != None:
                if int(current_node.value) not in visited_list:
                    stack.append(current_node)
                    visited_list.append(int(current_node.value))
                current_node = current_node.next

        while len(stack) != 0:
            return_node = stack.pop()
            print(return_node.value)
