# Problem 1 - Greedy MAB Player

## 1. Expectations 

Our expectations for the Greedy MAB Player are that the player quickly decides on an action that it continues to perform because it has received the most wins from that action over the number of times that action has been taken. We expect that the graph will increase ("lucky") or decrease ("unlucky") rapidly until it hits a point where it will stay the same because it has found the action it thinks is best, even without experimenting with the other actions as much as it maybe should.

## 2. Sim Results

# Problem 2 - ϵ-Greedy MAB Player

## 1. Expectations 

Our expectations for the epsilon-greedy MAB Player are that it performs well, since it gets to experiement more than greedy to find the best action, but will not reach the highest cumulative reward that it can because it keeps exploring for a percentage of epsilon amount of trials even after the optimal action is found.

## 2. Sim Results
Epsilon Greedy where E = 0.05
![EGreedy0 05](https://user-images.githubusercontent.com/21330088/55663455-de8c5c00-57d2-11e9-90ec-a1c394015882.jpeg)

Epsilon Greedy where E = 0.1
![EGreedy0 1](https://user-images.githubusercontent.com/21330088/55663454-de8c5c00-57d2-11e9-91a3-823d8ac2abed.jpeg)

Epsilon Greedy where E = 0.15
![EGreedy0 15](https://user-images.githubusercontent.com/21330088/55663456-de8c5c00-57d2-11e9-9656-1cae28740c4a.jpeg)

# Problem 3 - ϵ-First MAB Player

## 1. Expectations 

Our expectations for the epsilon-first MAB Player are that it will explore all actions for a certain amount of time (N) (flat line in the middle of the graph) and then will rapidly increase to a very high number because it will have figured out the best action at that point.

## 2. Sim Results


# Problem 4 - ϵ-Decreasing MAB Player

## 1. Expectations 

Our expectations for the epsilon-decreasing MAB Player are that it will perform very well. Because it explores a lot at the beginning to find the best action, and then continues exploring as time goes on, gives in a good chance of finding the true optimal action. Epsilon-decreasing also means that eventually the MAB Player will stop exploring other options, which makes it better than epsilon-greedy in the long run.

## 2. Sim Results

# Problem 5 - Thompson Sampling MAB Player

## 1. Expectations 

## 2. Sim Results

## 3. Compare

## 4. Reflect


