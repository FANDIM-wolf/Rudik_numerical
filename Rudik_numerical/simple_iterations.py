import numpy as np
def calculate_with_simple_iterations(A, b):
    # Check for compatibility
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix should be square")
    
    n = A.shape[0]
    x = np.zeros(n)
    
    for i in range(n):
        sum = 0
        for j in range(n):
            if i != j:
                sum += A[i, j] * x[j]
        
        x[i] = (b[i] - sum) / A[i, i]
    
    return x

# Example of use
#A = np.array([[2, 4,1], [3, 6,1] , [3,1,1]])
#b = np.array([8, 15 ,10])
#x = simple_iterations(A, b)
#print(x)