# Problem 1 - Greedy MAB Player

## 1. Expectations 

Our expectations for the Greedy MAB Player are that the player quickly decides on an action that it continues to perform because it has received the most wins from that action over the number of times that action has been taken. We expect that the graph will increase ("lucky") or decrease ("unlucky") rapidly until it hits a point where it will stay the same because it has found the action it thinks is best, even without experimenting with the other actions as much as it maybe should.

## 2. Sim Results
**IGNORE THE BLUE, GREEDY GRAPH IS IN RED - Forgot to screenshot greedy only.**
![GREEDYISRED](https://user-images.githubusercontent.com/21330088/55663791-fa463100-57d7-11e9-94e2-e3576e6e88cd.jpeg)

# Problem 2 - ϵ-Greedy MAB Player

## 1. Expectations 

Our expectations for the epsilon-greedy MAB Player are that it performs well, since it gets to experiement more than greedy to find the best action, but will not reach the highest cumulative reward that it can because it keeps exploring for a percentage of epsilon amount of trials even after the optimal action is found. For smaller values of epsilon such as 0.05, the agent does less exploring and therefore would perform more like the Greedy player, while the higher values of epsilon will do more exploring.

## 2. Sim Results
Epsilon Greedy where ε = 0.05
![EGreedy0 05](https://user-images.githubusercontent.com/21330088/55663455-de8c5c00-57d2-11e9-90ec-a1c394015882.jpeg)

Epsilon Greedy where ε = 0.1
![EGreedy0 1](https://user-images.githubusercontent.com/21330088/55663454-de8c5c00-57d2-11e9-91a3-823d8ac2abed.jpeg)

Epsilon Greedy where ε = 0.15
![EGreedy0 15](https://user-images.githubusercontent.com/21330088/55663456-de8c5c00-57d2-11e9-9656-1cae28740c4a.jpeg)

# Problem 3 - ϵ-First MAB Player

## 1. Expectations 

Our expectations for the epsilon-first MAB Player are that it will explore all actions for a certain amount of time (N) (flat line in the middle of the graph) and then will rapidly increase to a very high number because it will have figured out the best action at that point. We used the same values for epsilon that we did in ε-Greedy to see the difference on performance between the two. We expect ε-First to perform better, given the same ε values because it is given more time to explore before choosing a best action to exploit, and once it finds that action, it no longer has to explore.

## 2. Sim Results
Epsilon First where ε = 0.05
![EFirst0 05](https://user-images.githubusercontent.com/21330088/55663504-902b8d00-57d3-11e9-920e-95659db989ac.jpeg)

Epsilon First where ε = 0.1
![EFirst0 1](https://user-images.githubusercontent.com/21330088/55663503-902b8d00-57d3-11e9-9604-1ed17f524229.jpeg)

Epsilon First where ε = 0.15
![EFirst0 15](https://user-images.githubusercontent.com/21330088/55663505-90c42380-57d3-11e9-9e23-72fd473e6f55.jpeg)

# Problem 4 - ϵ-Decreasing MAB Player

## 1. Expectations 

Our expectations for the epsilon-decreasing MAB Player are that it will perform very well because it explores a lot at the beginning to find the best action, and then continues exploring as time goes on, gives in a good chance of finding the true optimal action. Epsilon-decreasing also means that eventually the MAB Player will stop exploring other options, which makes it better than epsilon-greedy in the long run. We started our ε at 0.1 for each cooling schedule that we reported in a graph below. We experimented with decreasing ε by a value of 0.0001, 0.001, and 0.01, or having ε decrease 1,000 times, 100 times, and 10 times, respectively. When decreasing ε by 0.0001, we have a slow decrease before we hit Greedy, decreasing by 0.001 is a quicker decrease, and the quickest is 0.1 where ε only decreases 10 times. We found that with the slower decrease (0.0001), the graph is a smoother curve, while with the super fast decrease you can barely see the jump from exploration to exploitation on the graph.

## 2. Sim Results
Epsilon Decreasing where ε decreases by -0.0001 each time
![EDecrease-0 0001](https://user-images.githubusercontent.com/21330088/55663521-db45a000-57d3-11e9-9181-4551c87c351b.jpeg)

Epsilon Decreasing where ε decreases by -0.001 each time
![EDecrease-0 001](https://user-images.githubusercontent.com/21330088/55663523-db45a000-57d3-11e9-87ba-2429eaaf9d94.jpeg)

Epsilon Decreasing where ε decreases by -0.01 each time
![EDecrease-0 01](https://user-images.githubusercontent.com/21330088/55663522-db45a000-57d3-11e9-8e10-ead3600d4c57.jpeg)

# Problem 5 - Thompson Sampling MAB Player

## 1. Expectations 

## 2. Sim Results

## 3. Compare

## 4. Reflect


