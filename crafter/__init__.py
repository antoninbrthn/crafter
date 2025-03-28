from .env import Env
from .recorder import Recorder

__version__ = "1.8.3+farm"  # farming mod

try:
  import gym
  gym.register(
      id='CrafterReward-v1',
      entry_point='crafter:Env',
      max_episode_steps=10000,
      kwargs={'reward': True})
  gym.register(
      id='CrafterNoReward-v1',
      entry_point='crafter:Env',
      max_episode_steps=10000,
      kwargs={'reward': False})
except ImportError:
  pass
