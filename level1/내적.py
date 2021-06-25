import numpy as np

def solution(a, b):
    
    a = np.array(a)
    b = np.array(b)

    return np.int(a.dot(b))
