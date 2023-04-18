import math
from itertools import permutations


def tsp(matrix):
    min_cost, best_path = float('inf'), []
    for perm in permutations(range(len(matrix))):
        cost = sum(matrix[perm[i]][perm[i + 1]] for i in range(len(matrix) - 1)) + matrix[perm[-1]][perm[0]]
        if cost < min_cost:
            min_cost, best_path = cost, perm
    return min_cost, best_path 


with open('matrix.txt', 'r') as f:
    matrix = [[int(num) for num in line.split()] for line in f.readlines()]

t=tsp(matrix)
print(t)