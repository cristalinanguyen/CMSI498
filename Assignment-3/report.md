## Problem 2

**1. P(Z|do(X))**

Yes, the query is identifiable where the back-door admissible adjusment set is Z = {A}. The adjustment formula used to compute the causal query would be P(Z|do(X)) = SUM_a * P(Z = z | X = x, A = a)P(A = a)

**2. P(B|do(A))**

Yes, it is identifiable but the back-door admissible set is the empty set where Z = {}. The adjustment formula used to compute the causal query would be P(B|do(A)) = P(B|A).

**3. P(Z|do(C))**

Yes, the query is identifiable where the back-door admissible adjustment set is Z = {B}. The adjustment formula used to compute the causal query would be P(Z|do(C)) = SUM_b * P(Z = z| C = c, B = b)P(B = b).

**4. P(Z|do(A))**

