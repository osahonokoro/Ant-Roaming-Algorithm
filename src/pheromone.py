def evaporate_pheromone(G, alpha=0.1, beta=0.05):
    for node in G.nodes:
        neglect = G.nodes[node]['last_visit']
        G.nodes[node]['pheromone'] = (1 - alpha) * G.nodes[node]['pheromone'] + beta * neglect

def deposit_pheromone(G, node, delta=0.1, Tmin=0.5):
    G.nodes[node]['pheromone'] = max((1 - delta) * G.nodes[node]['pheromone'] + Tmin, Tmin)
