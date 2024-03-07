import random

class Agent:
    def __init__(self, agent_id, strategy):
        self.id = agent_id
        self.action = None
        self.reward_history = []
        self.strategy = Strategy(strategy)

    def choose_action(self):
        self.action = self.strategy.choose_action(self.reward_history)

class Strategy:
    def __init__(self, strategy_type):
        if strategy_type == "tit_for_tat":
            self.strategy_func = self.tit_for_tat
        else:
            self.strategy_func = self.benevolent_tit_for_tat

    def choose_action(self, reward_history):
        return self.strategy_func(reward_history)

    def tit_for_tat(self, reward_history):
        if not reward_history:
            return random.choice(["cooperate", "defect"])
        elif reward_history[-1] == 2:
            return "cooperate"
        else:
            return "defect"

    def benevolent_tit_for_tat(self, reward_history):
        if len(reward_history) < 2:
            return random.choice(["cooperate", "defect"])
        elif reward_history[-1] == 2:
            return "cooperate"
        elif reward_history[-2] == 0:
            return "defect"
        else:
            return "cooperate"

class Environment:
    def two_player_reward_map(self, agents):
        p1_action = agents[0].action
        p2_action = agents[1].action
        if p1_action == "cooperate":
            if p2_action == "defect":
                return [0, 1]
            else:
                return [2, 2]
        else:
            if p2_action == "cooperate":
                return [1, 0]
            else:
                return [0, 0]

    def __init__(self, num_agents, actions):
        self.num_agents = num_agents
        self.actions = actions
        self.agents = [Agent(i, "benv") for i in range(num_agents)]

    def run(self):
        for agent in self.agents:
            agent.choose_action()

        rewards = self.two_player_reward_map(self.agents)
        for agent in self.agents:
            agent.reward_history.append(rewards[agent.id])

        return rewards

# Example usage
num_agents = 2
total_rewards = [0 for _ in range(num_agents)]
actions = ["cooperate", "defect"]
env = Environment(num_agents, actions)

for _ in range(1000):
    rewards = env.run()

    for agent in env.agents:
        print(f"Agent {agent.id}: Action - {agent.action}, Reward - {rewards[agent.id]}")
        total_rewards[agent.id] += rewards[agent.id]

print("In the end...")
print(total_rewards)
