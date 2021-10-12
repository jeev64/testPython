import statistics

import numpy as np
import pandas as pd

b = [0,1,2,3,4,5,6,7]
#c = ([2,6,2,8,4,0,1,])

#a = np.array([0,1,2,3,4,5,6,7,8])
#a = np.array([2,6,2,8,4,0,1,5,7])

if len(b) != 9:
    #return "List must contain nine numbers."
    print(["List must contain nine numbers.", b])


x = np.array(b).reshape(3, 3)
result = {
    k: [func(x, axis=ax).tolist()
        for ax in [0, 1, None]]
    for (k, func)
    in zip(["mean", "variance", "standard deviation", "max", "min", "sum"],
           [np.mean, np.var, np.std, np.max, np.min, np.sum])




}

print(result)



