import pandas as pd
import numpy as np


def hello():
    return "hello world"


result = hello()
print(result)

a = np.array([0, 1, 2, 3, 4])


def cal():
    return {
        'means': np.mean(a),
        'average': 3 * 5}


result1 = cal()
print(result1)
