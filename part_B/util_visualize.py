'''
Here are helper functions that use networkx package to visualize the graphs and
helper functions to convert adjacency list network representation to networkx G
'''

import networkx as nx
import matplotlib.pyplot as plt

# Created networkx Graph from adjacency list network representation
def create_G_from_network(network):
    G = nx.Graph()

    for u, neighbours in network.items():
        for v, w in neighbours:
            G.add_edge(u, v, weight=w)
    return G

# plots networkx Graph using networkx capabilities
def plot_graph(G, title):
    plt.figure(figsize=(8,6))
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1000)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,font_color='darkgreen', label_pos=0.4)
    plt.title(title)

    plt.show()

def create_G_from_mst(mst):
    """
    Creates nx Graph from list of weighted edges (u, v, w)
    """
    G = nx.Graph()
    G.add_weighted_edges_from(mst)
    return G

# Visualize MST within the original network
def plot_mst(G, mst_G, title):

    plt.figure(figsize=(8,6))
    pos = nx.circular_layout(G)

    # Draw original network
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1000)
    nx.draw_networkx_labels(G, pos, )
    nx.draw_networkx_edges(G, pos, edge_color='gray')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,font_color='black', label_pos=0.4)

    # Highlight MST
    nx.draw_networkx_edges(mst_G, pos, width=8, edge_color='tan', alpha=0.3)

    plt.title(title, fontsize=14, pad=20)
    plt.tight_layout()

    plt.show()