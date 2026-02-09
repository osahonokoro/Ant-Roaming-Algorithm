import gymnasium as gym
from gymnasium import spaces
import numpy as np
from environment import create_environment
from pheromone import evaporate_pheromone, deposit_pheromone
from patrol import choose_next_node
from reward import calculate_reward

class ARAEnv(gym.Env):
    def __init__(self, steps=50):
        super(ARAEnv, self).__init__()
        self.steps = steps
        self.current_step = 0
        self.G = create_environment()
        self.current_node = 0
        self.path = [self.current_node]
        self.incidents = []
        self.compliance = 1.0  # placeholder

        # Observation space: pheromone + risk for each node
        self.observation_space = spaces.Box(low=0, high=1,
                                            shape=(len(self.G.nodes), 2),
                                            dtype=np.float32)

        # Action space: choose next node among neighbors
        self.action_space = spaces.Discrete(len(self.G.nodes))

    def reset(self):
        self.current_step = 0
        self.G = create_environment()
        self.current_node = 0
        self.path = [self.current_node]
        self.incidents = []
        self.compliance = 1.0
        return self._get_obs()

    def _get_obs(self):
        obs = []
        for node in self.G.nodes:
            obs.append([self.G.nodes[node]['pheromone'],
                        self.G.nodes[node]['risk']])
        return np.array(obs, dtype=np.float32)

    def step(self, action):
        self.current_step += 1

        # Evaporate pheromone
        evaporate_pheromone(self.G)

        # Move to chosen node
        if action in self.G.neighbors(self.current_node):
            next_node = action
        else:
            next_node = choose_next_node(self.G, self.current_node)

        deposit_pheromone(self.G, next_node)
        self.path.append(next_node)
        self.current_node = next_node

        # Example incident: node 5 triggers anomaly
        if self.current_node == 5:
            self.incidents.append({"step": self.current_step, "node": self.current_node})

        # Calculate reward
        reward = calculate_reward(agent="A1",
                                  coverage=len(set(self.path)),
                                  incidents=self.incidents,
                                  compliance=self.compliance)

        done = self.current_step >= self.steps
        return self._get_obs(), reward, done, {}

