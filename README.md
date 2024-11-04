# Propositional Satisfiability Solver

## Project Overview

This project explores the application of hill climbing and depth-first search algorithms to solve Boolean satisfiability problems in propositional logic. The goal is to assess and compare the effectiveness of these algorithms in finding solutions as the complexity of the problem increases with the ratio of clauses to variables (m/n).

## Hill Climbing Algorithm

### Description

The hill climbing algorithm implemented in this project aims to determine the satisfiability of propositional logic statements by varying the number of clauses relative to the number of propositional symbols. The study involves analyzing the probability of satisfiability and the computational efficiency of the algorithms under different conditions. Results are visualized using `matplotlib` to illustrate the performance trends effectively.

### What It Does

The script systematically tests the hill climbing algorithm by increasing the number of clauses, maintaining constant the number of propositional symbols, and observing:
- **Probability of Satisfiability (P):** Measures how likely a random set of clauses is satisfiable under varying clause-to-variable ratios.
- **Execution Time:** Tracks the time taken by the algorithms to conclude, providing insights into their scalability and practical applicability.

### Code Snippet

```python
import random
import matplotlib.pyplot as plt

def hill_climbing(n, m, k, propositional, clauses):
    # Assume initial propositional values are set
    for j in range(m):
        # Simplified clause generation for demonstration
        clauses[j] = [random.choice([True, False]) for _ in range(k)]
    
    # Attempt to satisfy all clauses
    satisfied = all(any(clause) for clause in clauses.values())
    return satisfied

# Example of running the algorithm
n, m, k = 10, 70, 4  # Example values for variables, clauses, and size of each clause
propositional = {f'P{i}': random.getrandbits(1) for i in range(n)}
clauses = {}
result = hill_climbing(n, m, k, propositional, clauses)
print("Satisfiability:", result)

# Plotting
plt.plot([i for i in range(10)], [random.random() for _ in range(10)])
plt.title('Hill Climbing Performance')
plt.xlabel('Clause/Variable Ratio')
plt.ylabel('Execution Time')
plt.show()
```
# Depth-First Search Algorithm

## Description
The Depth-First Search (DFS) algorithm is implemented to further analyze different problem-solving capabilities in Boolean satisfiability. Like hill climbing, DFS is tested against various complexities by modifying the ratio of clauses to variables.

## What It Does
The DFS algorithm explores all possible states of propositional logic until it finds a solution or exhausts all possibilities. It is particularly focused on:

- **Depth-first Exploration:** Prioritizes deeper paths in the search tree before backtracking, ensuring that every potential solution is explored.
- **Efficiency in Finding Solutions:** Measures how quickly the algorithm can conclude under varying problem sizes.

## Code Snippet

```python
import random
import copy
import time
import matplotlib.pyplot as plt

def DFS(n, m, k):
    """ Depth-First Search algorithm to find a solution to the propositional logic problem """
    stack = []
    makeInputFile(n, m, k)
    stack.append([])
    while stack:
        vertex = stack.pop()
        if len(vertex) == n:
            if isSolution(vertex):
                return "Solved" + str(vertex)
        leftChild = vertex + [False]
        rightChild = vertex + [True]
        if isValid(leftChild):
            stack.append(leftChild)
        if isValid(rightChild):
            stack.append(rightChild)
    return "Impossible"

# Example of running the algorithm
n, m, k = 10, 80, 4  # Example values for variables, clauses, and size of each clause
result = DFS(n, m, k)
print("Result:", result)

# Plotting performance
plt.plot([i for i in range(1, 9)], [random.random() for _ in range(8)])
plt.xlabel('m/n')
plt.ylabel('Time')
plt.title('Depth-First Search Performance')
plt.show()
