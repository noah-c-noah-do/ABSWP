import random
from random import expovariate

coin = [0, 1]
n = int(input("Enter the number of coin flips: "))

experiment_results = ''
for i in range(n):
    experiment_results += str(random.choice(coin))

print(experiment_results)
zeros = experiment_results.count('000000')
print(zeros)
ones = experiment_results.count('111111')
print(ones)
streaks = zeros + ones
print(f'Chance of streak: {(zeros + ones) / n}')
