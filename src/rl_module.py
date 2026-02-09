import gym
from stable_baselines3 import PPO

def train_rl(env):
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)
    return model
