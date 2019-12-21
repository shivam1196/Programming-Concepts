"""
A program written in python which creates a tree based upon the given input using the adjacency list concept
"""
from Graphs.GraphTraversal import GraphTraversal
from Graphs.Node import Node

vertex_list = []


def create_graph(vertex_number, edge_list):
    global vertex_list
    head_node = Node(vertex_number)
    vertex_list.append(head_node)
    current_node = head_node
    for i in range(0, len(edge_list)):
        temp_node = Node(edge_list[i])
        current_node.next = temp_node
        current_node = temp_node


if __name__ == "__main__":
    number_of_vertex = input("Enter number of vertex\n")
    number_of_edge = []
    for i in range(int(number_of_vertex)):
        number_of_edge = input().split(" ")
        create_graph(i + 1, number_of_edge)

    graph_traversal = GraphTraversal()
    graph_traversal.bfs(vertex_list)
