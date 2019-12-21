from Graphs.GraphQueue import GraphQueue


class GraphTraversal:

    def bfs(self, adjacency_list):
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
