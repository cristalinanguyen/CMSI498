# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util, random

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        for k in range(self.iterations):
            # Counter that holds the values for this iteration
            valuez = util.Counter()
            for current in mdp.getStates():
                # Counter that holds four sums -> one for each action
                sums = util.Counter()
                for action in mdp.getPossibleActions(current):
                    transition = mdp.getTransitionStatesAndProbs(current, action)
                    sum = 0
                    # for each possible transition
                    for i in range(len(transition)):
                        prob = transition[i][1]
                        nextState = transition[i][0]
                        product = prob * (mdp.getReward(current, action, nextState) + self.discount * self.values[nextState])
                        # add all the products together - there are multiple s' (nextState) because of the transition probabilities
                        sum += product
                    # store the sum and action together
                    sums[action] = sum
                # print sums
                maxA = sums.argMax()
                # the new state value is the value of the max action
                valuez[current] = sums[maxA]
            # replace self.values with the values just computed in the past iteration (stored in valuez)
            for state in mdp.getStates():
                self.values[state] = valuez[state]
        print self.values

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        # because this is the exact same code from above used in value iteration create a Bellman helper method (?)
        # or does that not work because one is in the constructor?
        transition = self.mdp.getTransitionStatesAndProbs(state, action)
        sum = 0
        # for each possible transition
        for i in range(len(transition)):
            prob = transition[i][1]
            nextState = transition[i][0]
            product = prob * (self.mdp.getReward(state, action, nextState) + self.discount * self.getValue(nextState))
            # add all the products together - there are multiple s' (nextState) because of the transition probabilities
            sum += product

        return sum

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        sums = util.Counter()
        for action in self.mdp.getPossibleActions(state):
            sums[action] = self.computeQValueFromValues(state, action)
        return sums.argMax()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
