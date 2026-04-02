import numpy as np
from numpy.typing import NDArray
import math

class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        arr = []
        for num in z:
            arr.append(round(1/(1+(math.e**(-num))),5))
        return arr
    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        arr = []
        for num in z:
            arr.append(np.maximum(0,num))
        return arr
        
