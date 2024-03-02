# a function to view a floor using networkx and matplotlib.pyplot
import networkx as nx
import matplotlib.pyplot as plt


def graph_from_matrix(graph_matrix):  # takes in a matrix, draws a graph. only works for undirected graphs
    node_num = len(graph_matrix)
    output_graph = nx.Graph()
    for i in range(node_num):
        output_graph.add_node(str(i))  # adds the nodes

    for i in range(node_num - 1):  # -1 because checking the last row is redundant
        redundancy_buffer = i + 1  # we don't start at the beginning of the array, because the first few
        # items are redundant because of previous lines, and no room connects to itself.
        j_range = node_num - redundancy_buffer
        for j in range(j_range):
            if graph_matrix[i][j + redundancy_buffer] == 1:
                output_graph.add_edge(str(i), str(j + redundancy_buffer))
    return output_graph


def display_graph(graph):
    nx.draw(graph, with_labels=True, node_color="black", node_size=1500, font_color="white", font_size=15,
            font_family="Times "
                        "New "
                        "Roman",
            font_weight="bold", width=5)
    plt.margins(0.2)
    plt.show()


def test():
    begin_array = [[0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 1, 0, 0],
                   [1, 1, 0, 0, 0, 1],
                   [0, 1, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 1],
                   [0, 0, 1, 0, 1, 0]]
    new_graph = graph_from_matrix(begin_array)
    display_graph(new_graph)

