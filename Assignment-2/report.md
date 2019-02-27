## Problem 1

1.
**Sleep Study:**
![sleep_study](https://user-images.githubusercontent.com/21330088/52664367-b44aac00-2ebd-11e9-87cc-0845cfafcbe7.jpeg)
**Study Study:**
![study_study](https://user-images.githubusercontent.com/21330088/52664368-b44aac00-2ebd-11e9-91fc-6ceff6438cb2.jpeg)
**Survey:**
![survey](https://user-images.githubusercontent.com/21330088/52664369-b44aac00-2ebd-11e9-8f4f-4a6ac7075956.jpeg)

2. There is one undirected edge in these graphs and it is on the study_study (study group) graph. This edge is between W and X. W is whether or not an individual got a 8+ hours of sleep before the exam and X is whether or not an individual exercised the day before the exam. This edge was not able to be oriented because 

## Problem 2

**1. P(Z|do(X))**

Yes, the query is identifiable where the back-door admissible adjusment set is Z = {A}. The adjustment formula used to compute the causal query would be P(Z|do(X)) = SUM_a P(Z = z | X = x, A = a)P(A = a).

**2. P(B|do(A))**

No, this is not identifiable using the back-door criterion. There is no way to stop the flow of information between A and B because we cannot condition on the unobserved confounder.

**3. P(Z|do(C))**

Yes, the query is identifiable where the back-door admissible adjustment set is Z = {B, X}. The flow of information from C to W to B to Z is blocked when we know by. By knowing B, however, we open the flow of information from B to U to A to X to Y to Z and from B to X to Y to Z. If we know X, the flow of information is blocked from B to Z. The adustment formula used to compute the causal query would be P(Z|do(C)) = SUM_b P(Z = z | C = c, B = b, X = x)P(B = b, X = x).

**4. P(Z|do(A))**

Yes, the query is identifiable where the back-door admissible adjustment set is Z = {B}. The adjustment formula used to compute the causal query would be P(Z|do(A)) = SUM_b P(Z = z | A = a, B = b)P(B = b).

