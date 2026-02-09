from stable_baselines3 import PPO
from ara_env import ARAEnv

def simulate():
    env = ARAEnv(steps=50)
    model = PPO.load("ara_ppo_model")
    obs = env.reset()

    for _ in range(50):
        action, _ = model.predict(obs)
        obs, reward, done, _ = env.step(action)
        if done:
            break

    print("Final Path:", env.path)
    print("Total Reward:", reward)

if __name__ == "__main__":
    simulate()
