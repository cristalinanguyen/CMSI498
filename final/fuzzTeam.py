# AUTHORS: Amelia Jay, Liam Namba, Cristalina Nguyen, Christian Santander
# myTeam.py
# ---------
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

from captureAgents import CaptureAgent
import random, time, util
from game import Directions
import game
from util import nearestPoint, Counter
arguments = {}

#################
# Team creation #
#################

def createTeam(firstIndex, secondIndex, isRed,
               first = 'SmartOffensive', second = 'SmartDefensive', **args):
  if 'numTraining' in args:
    arguments['numTraining'] = args['numTraining']
  # The following line is an example only; feel free to change it.
  return [eval(first)(firstIndex), eval(second)(secondIndex)]

##########
# Agents #
##########

class SmartAgent(CaptureAgent):

  def __init__(self, index):
    CaptureAgent.__init__(self, index)
    self.weights = util.Counter()
    self.numTraining = 0
    self.episodesSoFar = 0
    self.epsilon = 0.05
    self.discount = 0.8
    self.alpha = 0.2

  def registerInitialState(self, gameState):
    self.start = gameState.getAgentPosition(self.index)
    CaptureAgent.registerInitialState(self, gameState)

  def chooseAction(self, gameState):
    actions = gameState.getLegalActions(self.index)
    # You can profile your evaluation time by uncommenting these lines
    # start = time.time()
    values = [self.evaluate(gameState, a) for a in actions]
    # print 'eval time for agent %d: %.4f' % (self.index, time.time() - start)
    maxValue = max(values)
    bestActions = [a for a, v in zip(actions, values) if v == maxValue]

    foodLeft = len(self.getFood(gameState).asList())

    if foodLeft <= 2:
      bestDist = 9999
      for action in actions:
        successor = self.getSuccessor(gameState, action)
        pos2 = successor.getAgentPosition(self.index)
        dist = self.getMazeDistance(self.start,pos2)
        if dist < bestDist:
          bestAction = action
          bestDist = dist
      return bestAction
    return random.choice(bestActions)

  def getSuccessor(self, gameState, action):
    """
    Finds the next successor which is a grid position (location tuple).
    """
    successor = gameState.generateSuccessor(self.index, action)
    pos = successor.getAgentState(self.index).getPosition()
    if pos != nearestPoint(pos):
      # Only half a grid position was covered
      return successor.generateSuccessor(self.index, action)
    else:
      return successor

  def evaluate(self, gameState, action):
    """
    Computes a linear combination of features and feature weights
    """
    features = self.getFeatures(gameState, action)
    weights = self.getWeights(gameState, action)
    return features * weights

  def getFeatures(self, gameState, action):
    """
    Returns a counter of features for the state
    """
    features = util.Counter()
    successor = self.getSuccessor(gameState, action)
    features['successorScore'] = self.getScore(successor)
    return features

  def getWeights(self, gameState, action):
    """
    Normally, weights do not depend on the gamestate.  They can be either
    a counter or a dictionary.
    """
    return {'successorScore': 1.0}

  def getQValue(self, state, action):
    features = self.featExtractor.getFeatures(state, action)
    weights = self.getWeights()
    dot = features * weights
    return dot

  def update(self, state, action, nextState, reward):
    maxVal = self.computeValueFromQValues(nextState)
    qValue = self.getQValue(state, action)
    diff = (reward + self.discount * maxVal) - qValue
    featuresDict = self.featExtractor.getFeatures(state, action)
    features = []
    for f in featuresDict:
      features.append(f)
    for f in features:
      self.weights[f] = self.weights[f] + self.alpha * diff * featuresDict[f]

class SmartOffensive(SmartAgent):
  def getFeatures(self, gameState, action):
    global agent_info
    successor = self.getSuccessor(gameState, action)
    is_pacman = successor.getAgentState(self.index).isPacman
    feature_names = ['successorScore', 'distanceToFood', 'ghostDistance', 'stop', 'distanceToSpawn']
    features = util.Counter()
    for name in feature_names:
      features[name] = 0
    # Score of Successor
    foodList = self.getFood(successor).asList()
    features['successorScore'] = -len(foodList)
    if action == Directions.STOP: features['stop'] = 1

    # Distance to opponents ghost
    myPos = successor.getAgentState(self.index).getPosition()
    opponentAgents = [successor.getAgentState(i) for i in self.getOpponents(successor)]
    dists = []
    ghosts = [a for a in opponentAgents if not a.isPacman and a.getPosition()]
    # if there are ghosts
    features['ghostDistance'] = min([self.getMazeDistance(myPos, a.getPosition()) for a in ghosts]) if ghosts and is_pacman else -1

    #Distance to closest food
    if len(foodList) > 0:  # This should always be True,  but better safe than sorry
      myPos = successor.getAgentState(self.index).getPosition()
      minDistance = min([self.getMazeDistance(myPos, food) for food in foodList])
      features['distanceToFood'] = minDistance

    # Carrying capacity
    numCarry = 20 - len(self.getFood(gameState).asList()) - self.getScore(successor)
    goHome = 0
    if numCarry >= 1:
      goHome = 1
    else:
      goHome = 0

    features['distanceToSpawn'] = goHome * self.getMazeDistance(myPos, gameState.getInitialAgentPosition(self.index))
    return features

  def getWeights(self, gameState, action):
    return {'successorScore': 10, 'distanceToFood': -1, 'ghostDistance': 5, 'stop': -100, 'distanceToSpawn': -10}

class SmartDefensive(SmartAgent):
  def getFeatures(self, gameState, action):
    feature_names = ['invaderDistance', 'onDefense', 'stop', 'reverse', 'distanceToMyFood']
    features = util.Counter()
    successor = self.getSuccessor(gameState, action)
    myState = successor.getAgentState(self.index)
    myPos = myState.getPosition()
    oppFoodList = self.getFoodYouAreDefending(successor).asList()

    for name in feature_names:
      features[name] = 0

    if len(oppFoodList) > 0:  # This should always be True,  but better safe than sorry
      myPos = successor.getAgentState(self.index).getPosition()
      minDistance = min([self.getMazeDistance(myPos, food) for food in oppFoodList])
      features['distanceToMyFood'] = minDistance

    features['onDefense'] = 1
    if myState.isPacman: features['onDefense'] = 0

    if action == Directions.STOP: features['stop'] = 1
    rev = Directions.REVERSE[gameState.getAgentState(self.index).configuration.direction]
    if action == rev:features['reverse'] = 1

    # Computes distance to invaders we can see
    enemies = [successor.getAgentState(i)for i in self.getOpponents(successor)]
    invaders = [a for a in enemies if a.isPacman and a.getPosition() != None]
    if len(invaders) > 0:
      dists = [self.getMazeDistance(myPos, a.getPosition()) for a in invaders]
      features['invaderDistance'] = min(dists)

    return features

  def getWeights(self, gameState, action):
    return {'invaderDistance': -10, 'onDefense': 100, 'stop': -100, 'reverse': -2, 'distanceToMyFood': -0.85}
