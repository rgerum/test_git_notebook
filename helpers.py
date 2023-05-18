import numpy as np

def calculate_average(x):
    a = 0
    for value in x:
        a += value
    return a / len(x)
