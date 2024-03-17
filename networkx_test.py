import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

seed = 2774
random.seed(seed)
np.random.seed(seed)

G = nx.Graph()
G.add_node("1")
G.add_node("2")
G.add_node("3")
G.add_node("4")
G.add_node("5")

G.add_edge("1", "2")
G.add_edge("1", "3")
G.add_edge("1", "4")
G.add_edge("4", "3")
G.add_edge("5", "2")

nx.draw(G, with_labels=True, node_color="red", node_size=3000, font_color="white", font_size=20, font_family="Times "
                                                                                                             "New "
                                                                                                             "Roman",
        font_weight="bold", width=5)
plt.margins(0.2)
plt.show()
