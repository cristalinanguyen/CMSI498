'''
  mab_agent.py
  
  Agent specifications implementing Action Selection Rules.
'''
import numpy as np

# ----------------------------------------------------------------
# MAB Agent Superclasses
# ----------------------------------------------------------------

class MAB_Agent:
    '''
    MAB Agent superclass designed to abstract common components
    between individual bandit players (below)
    '''
    # history = Action 0: [win][loss]
    #           Action 1: [win][loss]
    #           Action 2: [win][loss]
    #           Action 3: [win][loss]
    history = [[0,0],[0,0],[0,0],[0,0]]
    #this is for the thompson sampling
    was_win = False
    def __init__ (self, K):
        # TODO: Placeholder: add whatever you want here
        self.K = K
    def give_feedback (self, a_t, r_t):
        '''
        Provides the action a_t and reward r_t chosen and received
        in the most recent trial, allowing the agent to update its
        history
        '''
        if r_t == 0:
            self.history[a_t][1] += 1
            self.was_win = False
        else: 
            self.history[a_t][0] += 1
            self.was_win = True
        return
    
    def clear_history(self):
        '''
        IMPORTANT: Resets your agent's history between simulations.
        No information is allowed to transfer between each of the N
        repetitions
        '''
        columns = 3
        rows = 1
        for i in range(columns):
            for j in range(rows):
                self.history[i][j] = 0

    # function to choose max
    def choose_max(self):
        max_index = 0
        if self.history[1][0] > self.history[0][0]:
            max_index = 1
        elif self.history[2][0] > self.history[1][0]:
            max_index = 2
        elif self.history[3][0] > self.history[2][0]:
            max_index = 3
        return max_index

    # update function for TS agent




# ----------------------------------------------------------------
# MAB Agent Subclasses
# ----------------------------------------------------------------
class Greedy_Agent(MAB_Agent):
    '''
    Greedy bandit player that, at every trial, selects the
    arm with the presently-highest sampled Q value
    '''
    def __init__ (self, K):
        MAB_Agent.__init__(self, K)
    
    def choose (self, *args):
        return self.choose_max()

class Epsilon_Greedy_Agent(MAB_Agent):
    '''
    Exploratory bandit player that makes the greedy choice with
    probability 1-epsilon, and chooses randomly with probability
    epsilon
    '''
    epsilon = 0
    def __init__ (self, K, epsilon):
        MAB_Agent.__init__(self, K)
        self.epsilon = epsilon
        
    def choose (self, *args):
        choice = 0
        rand = np.random.uniform(0,1)
        if (rand > self.epsilon):
            choice = self.choose_max()
        else:
            choice = np.random.choice(list(range(self.K)))
        return choice

class Epsilon_First_Agent(MAB_Agent):
    '''
    Exploratory bandit player that takes the first epsilon*T
    trials to randomly explore, and thereafter chooses greedily
    '''
    trials = 0
    def __init__ (self, K, epsilon, T):
        MAB_Agent.__init__(self, K)
        self.trials = epsilon * T
    def choose (self, *args):
        choice = 0
        if self.trials > 0:
            choice = np.random.choice(list(range(self.K)))
            self.trials -= 1
        else:
            choice = self.choose_max()
        return choice


class Epsilon_Decreasing_Agent(MAB_Agent):
    '''
    Exploratory bandit player that acts like epsilon-greedy but
    with a decreasing value of epsilon over time
    '''
    epsilon = 0.1
    def __init__ (self, K):
        MAB_Agent.__init__(self, K)
        
    def choose (self, *args):
        choice = 0
        rand = np.random.uniform(0,1)
        if (rand > self.epsilon):
            choice = self.choose_max()
        else:
            choice = np.random.choice(list(range(self.K)))
        self.epsilon -= 0.001
        return choice

class TS_Agent(MAB_Agent):
    '''
    Thompson Sampling bandit player that self-adjusts exploration
    vs. exploitation by sampling arm qualities from successes
    summarized by a corresponding beta distribution
    '''
    alpha = 1.0
    beta = 1.0
    # [[s1,f1],[s2,f2]...]
    weights = [[0,0],[0,0],[0,0],[0,0]]
    beta_dist = [0,0,0,0]
    last_choice = 0
    def __init__ (self, K):
        MAB_Agent.__init__(self, K)

    def choose (self, *args):
        #update the beta distributions
        self.update(self.last_choice, self.was_win)
        #choose the greatest beta dist
        choice = self.beta_dist.index(max(self.beta_dist))
        last_choice = choice
        return choice

    def update(self, last_choice, was_win):
        if was_win:
            self.weights[self.last_choice][0] += 1
        else:
            self.weights[self.last_choice][1] += 1
        #if last was a win increment the correct weight, either s1 or f1
        for i in range(len(self.beta_dist)):
            self.beta_dist[i] = np.random.beta(self.weights[i][0] + self.alpha, self.weights[i][1] + self.beta)