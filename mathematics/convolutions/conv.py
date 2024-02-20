''' Understanding 2D Convolutional Layers '''

# import modules 
import numpy as np

image_input = [[3, 4, 6, 0, 6, 5],
               [2, 7, 1, -1, 8, 7],
               [0, 9, 4, 8, 0, 6],
               [1, 2, 3, 6, 8, 4],
               [4, 3, 5, 3, 2, 1],
               [7, 5, -5, 0, 3, 6]]
image_input = np.array(image_input)
print(image_input.shape)
# filter to be swept over image input
kernel = [[1, 0, -1],
          [1, 0, -1],
          [1, 0, -1]]
kernel = np.array(kernel)

def conv_image(images, kernel):
    ''' Convolvs an image'''
    
    # get the shape of the images
    m = images.shape[0]
    image_height = 6
    image_width = 6

    kernel_height = 3
    kernel_width = 3

    conv_rows = (image_height - kernel_height) + 1
    conv_cols = (image_width - kernel_width) + 1

    conv_img = np.zeros((m, conv_rows, conv_cols), dtype=int)

    for i in range(conv_rows): # Iterate over rows
        for j in range(conv_cols): # Iterate over columns
            shadow_area = images[i:i+kernel_height, j:j+kernel_width]
            conv_img[:, i, j] = np.sum(shadow_area * kernel)

    return conv_img

print(conv_image(image_input, kernel))