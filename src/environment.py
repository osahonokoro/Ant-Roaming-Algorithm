import networkx as nx

def create_environment():
    G = nx.Graph()
    nodes = list(range(10))  # Example: 10 critical nodes
    G.add_nodes_from(nodes)

    # Sample edges (replace with actual campus map data)
    edges = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,0)]
    G.add_edges_from(edges)

    # Initialize node attributes
    for node in G.nodes:
        G.nodes[node]['risk'] = 0.5
        G.nodes[node]['last_visit'] = 0
        G.nodes[node]['priority'] = 1.0
        G.nodes[node]['pheromone'] = 1.0
    return G
