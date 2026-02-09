from environment import create_environment
from pheromone import evaporate_pheromone, deposit_pheromone
from patrol import choose_next_node
from reward import calculate_reward

def run_simulation(steps=50):
    G = create_environment()
    current = 0
    path = [current]
    incidents = []  # placeholder for incident events

    for t in range(steps):
        evaporate_pheromone(G)
        next_node = choose_next_node(G, current)
        deposit_pheromone(G, next_node)
        path.append(next_node)
        current = next_node

        # Example: mark incident if node == 5
        if current == 5:
            incidents.append({"step": t, "node": current})

    # Example compliance metric (placeholder)
    compliance = 0.8

    reward = calculate_reward(agent="A1",
                              coverage=len(set(path)),
                              incidents=incidents,
                              compliance=compliance)

    print("Patrol Path:", path)
    print("Reward Score:", reward)

if __name__ == "__main__":
    run_simulation()
