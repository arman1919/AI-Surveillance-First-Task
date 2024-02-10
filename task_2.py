# Մենակ նայել եմ ոնց numpy ով invert անե
# իմ իմացած ձևով երկար էր

import numpy as np


matrix = np.random.randint(0,2,size=[4,4])

print(matrix)

def flip_invert(matrix):
    
    # horizontal flipping
    matrix = matrix[::-1]   
    
    # invert
    matrix =  1 - matrix
    

    print(matrix)
    
    
    
print(matrix)    
print()
matrix = flip_invert(matrix)

print(matrix)


