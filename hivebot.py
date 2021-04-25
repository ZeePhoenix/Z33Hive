from pysc2.agents import base_agent
from pysc2.env import sc2_env, run_loop
from pysc2.lib import actions, features, units
from absl import app
import random

class HiveZ33(base_agent.BaseAgent):
	def step(self, obs):
		super(HiveZ33, self).step(obs)
		return actions.FUNCTIONS.no_op()

def main(unused_argv):
	agent = HiveZ33()
	try:
		with sc2_env.SC2Env(
				map_name="Simple64",
				players=[sc2_env.Agent(sc2_env.Race.zerg),
						 sc2_env.Bot(sc2_env.Race.random,sc2_env.Difficulty.very_easy)],
				agent_interface_format=features.AgentInterfaceFormat(
					feature_dimensions=features.Dimensions(screen=84, minimap=64),
					use_feature_units=True),
				step_mul=16,
				game_steps_per_episode=0,
				visualize=True) as env:
			run_loop.run_loop([agent], env)
	except KeyboardInterrupt:
			pass

if __name__ == "__main__":
	app.run(main)