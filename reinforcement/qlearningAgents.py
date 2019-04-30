# qlearningAgents.py
# ------------------
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


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math
import numpy as np

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        self.qValues = util.Counter() # Dictionary returns 0 by default

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        return self.qValues[(state, action)]

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        # Check if there are legal actions, if there are then return the max action from qValues
        # Otherwise return 0
        # getLegalActions() returns self.actionFn(state) [list of actions]

        legalActions = self.getLegalActions(state)
        options = util.Counter()

        # If there are no legal actions (list is empty), return 0.0
        if len(legalActions) < 1:
            return 0.0
        else:
            # Return the max key value from qValues
            for action in legalActions:
                options[(state, action)] = self.getQValue(state, action)

            # options.argMax() is a tuple (state, action) - key in dictionary
            max = options.argMax()

            # Value
            return options[max]

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        # max = options.argMax() is a tuple (state, action)
        # options[max] is a value

        # legalActions is a list of possible actions
        legalActions = self.getLegalActions(state)
        options = util.Counter()

        # If there are no legal actions, return None
        if len(legalActions) < 1:
            return None

        # Otherwise return the action at the key value in dictionary qValues
        else:
            # Return the max key value from qValues
            for action in legalActions:
                options[(state, action)] = self.getQValue(state, action)

            # options.argMax() is a tuple (state, action) - key in dictionary
            max = options.argMax()

            # Value
            return max[1]

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        options = util.Counter()

        # If there are no legal actions, return None
        if len(legalActions) < 1:
            return None

        else:
            # Return the max key value from qValues
            for action in legalActions:
                options[(state, action)] = self.getQValue(state, action)
            # options.argMax() is a tuple (state, action) - key in dictionary
            max = options.argMax()
            # Epsilon Greedy Part:
            if not(util.flipCoin(self.epsilon)):
                return max[1]
            else:
                return random.choice(legalActions)

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        # Q(s, a) + alpha(sample - Q(s, a))
        # q + self.alpha(sample - q)

        # sample = R(s, a, s') + discount * max_a'(Q(s, a))
        # sample = reward + self.discount * computeValueFromQValues(nextState)

        q = self.getQValue(state, action)

        # Compute sample
        maxVal = self.computeValueFromQValues(nextState)
        sample = reward + self.discount * maxVal

        # Update Q(s, a)
        self.qValues[(state, action)] = q + self.alpha * (sample - q)


    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """

        weight = self.getWeights()
        features = self.featExtractor.getFeatures(state, action)

        product = (weight) * (features)

        return product

    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        # difference = (reward + discount*computeValueFromQValues(nextState)) - getQValue(state, action)
        maxVal = self.computeValueFromQValues(nextState)
        qValue = self.getQValue(state, action)

        difference = (reward + self.discount * maxVal) - qValue

        featuresDict = self.featExtractor.getFeatures(state, action)
        features = []
        for f in featuresDict:
            features.append(f)

        for f in features:
            # weight = weight_i + alpha * difference * f_i(s, a)
            self.weights[f] = (self.weights[f] + self.alpha * difference * featuresDict[f])

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass
