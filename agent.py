import random

# Stag Hunt


class Agent:
    strategy = None
    def __init__(self, id,strategy_type):
        self.id = id
        self.action = None
        self.reward = []
        self.strategy = Strategy(strategy_type).strategy
        # self.strategy =None

    def choose_action(self, actions):
        # Replace this with your agent's decision-making logic based on game theory principles.
        # This example randomly chooses an action.

        ## This should be replaced with the strategy
        # self.action = random.choice(actions)
        self.action  = self.strategy(self.reward)
        
class Strategy:
    
    strategy = None
    
    def __init__(self, strategy_type):
        if strategy_type == "tit_for_tat":
            self.strategy = self.tit_for_tat
        else:
            self.strategy =  self.benevolent_tit_for_tat

    def tit_for_tat(self,reward):
        if reward ==[]:
            return random.choice(["cooperate","defect"])  ## Start with a random choice
        elif reward[-1] == 2:
            return "cooperate"
        else:
            return "defect"
        
    def benevolent_tit_for_tat(self,reward):
        if reward[-1] == 2: # Check for the last move
            return "cooperate"
        elif reward[-2] == 0:
            return "defect"
        else:
            return "cooperate"
        


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


        # Calculate rewards based on the chosen actions (replace with your game logic)
        rewards = {agent.id: 0 for agent in self.agents}  # Initialize all rewards to 0
        # ... (Implement your game logic to calculate rewards based on chosen actions)

        if num_agents == 2: #two player games
            rewards = self.two_player_reward_map(self.agents)
            for agent in self.agents:
                agent.reward.append(rewards[agent.id])
        
        # Update agent states based on rewards (optional)
        for agent in self.agents:
            # ... (Update agent state based on reward)
            print("reward")
            # print(agent.reward)
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
