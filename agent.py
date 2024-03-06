import random

# Stag Hunt


class Strategy:
    def __init__(self, strategy):
        if strategy == "tit_for_tat":
            return self.tit_for_tat()
        else:
            return self.benevolent_tit_for_tat()

    def tit_for_tat(self,last_5_moves):
        return last_5_moves[-1]
        
    def benevolent_tit_for_tat(self,last_5_moves):
        if last_5_moves[-1] == "cooperate": # Check for the last move
            return "cooperate"
        elif last_5_moves[-2] == "defect":
            return "defect"
        else:
            return "cooperate"

class Agent:
    def __init__(self, id,Strategy):
        self.id = id
        self.action = None
        self.reward = None
        self.strategy = Strategy

    def choose_action(self, actions):
        # Replace this with your agent's decision-making logic based on game theory principles.
        # This example randomly chooses an action.

        ## This should be replaced with the strategy
        self.action = random.choice(actions)

class Environment:
    
    def two_player_reward_map(self,Agent):
        p1_action = Agent[0].action
        p2_action = Agent[1].action
        if p1_action == "cooperate":
            if p2_action == "defect":
                return [0,1]
            else:
                return [2,2]
        else:
            if p2_action == "cooperate":
                return [1,0]
            else:
                return [0,0]
                
    def __init__(self, num_agents, actions):
        self.num_agents = num_agents
        self.actions = actions
        self.agents = [Agent(i,"tit_for_tat") for i in range(num_agents)]
        self.rewards = {agent.id: 0 for agent in self.agents}

    def run(self):
        # Agents choose actions simultaneously
        for agent in self.agents:
            agent.choose_action(self.actions)
            action_space = agent.action

        # Calculate rewards based on the chosen actions (replace with your game logic)
        rewards = {agent.id: 0 for agent in self.agents}  # Initialize all rewards to 0
        # ... (Implement your game logic to calculate rewards based on chosen actions)

        if num_agents == 2: #two player games
            rewards = self.two_player_reward_map(self.agents)
        # Update agent states based on rewards (optional)
        for agent in self.agents:
            # ... (Update agent state based on reward)
            print("reward")
            return rewards


# Example usage
num_agents = 2
total_rewards = [0 for i in range(num_agents)]
actions = ["cooperate", "defect"]
env = Environment(num_agents, actions)
i = 0
while(i < 1000):
    rewards = env.run()

    # Print the chosen actions and rewards for each agent
    for agent in env.agents:
        print(f"Agent {agent.id}: Action - {agent.action}, Reward - {rewards[agent.id]}")
        total_rewards[agent.id] = total_rewards[agent.id] + rewards[agent.id]

    i = i+1

print("In the end...")
print(total_rewards)
