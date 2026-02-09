import random

def choose_next_node(G, current, alpha_tau=1, alpha_eta=1, alpha_risk=1):
    neighbors = list(G.neighbors(current))
    weights = []
    for j in neighbors:
        tau = G.nodes[j]['pheromone']
        eta = 1.0 / (1.0 + G[current][j].get('distance',1))
        risk = G.nodes[j]['risk']
        weight = (tau ** alpha_tau) * (eta ** alpha_eta) * (risk ** alpha_risk)
        weights.append(weight)
    return random.choices(neighbors, weights=weights, k=1)[0]
