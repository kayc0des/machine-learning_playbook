# import modules 
import numpy as np

image_input = [[3, 4, 6, 0, 6, 5],
               [2, 7, 1, -1, 8, 7],
               [0, 9, 4, 8, 0, 6],
               [1, 2, 3, 6, 8, 4],
               [4, 3, 5, 3, 2, 1],
               [7, 5, -5, 0, 3, 6]]

image_input = np.array(image_input)

''' Movement across image input '''
k = 3
for i in range(4):
    for j in range(4):
        print(f'This is is the {i+1} row and the 3x3 matrix starting from {image_input[i][j]}\n')
        print(image_input[i:i+k, j:j+k])
