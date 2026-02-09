from stable_baselines3 import PPO
from ara_env import ARAEnv

def train_agent():
    env = ARAEnv(steps=50)
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=5000)
    model.save("ara_ppo_model")

if __name__ == "__main__":
    train_agent()
