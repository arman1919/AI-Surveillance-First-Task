
# չգիտեի  գրադարան որ  ստացված մատրիցը ցույց տար
# numpy  սովորել եմ lab ից
# validatia ն արած չի

import numpy as np
import matplotlib.pyplot as plt



def random_color(size):
    return np.random.randint(0, 256, size=size + [3])  


def show_image(matrix):
    plt.imshow(matrix)
    plt.show(block=False)  
    plt.waitforbuttonpress()


if __name__ ==  "__main__":
    matrix = random_color([10000,10000])
 
    while True:
       
        print("1) Change the RGB pixel values in the image coordinates (x, y)")
        print("2) Get the RGB pixel values in the image coordinates (x, y)")
        print("3) Show the image by printing the pixel color values of the image")
        sel = input("Select option :")
        
        if sel == "1":
            x  = int(input("Enter x : ")) 
            y  = int(input("Enter y : "))

            R = int(input("Enter cllor  R:"))
            G = int(input("Enter cllor  G:"))
            B = int(input("Enter cllor  B:"))
            
            matrix[x][y] = [R,G,B]
        
        elif sel == "2":
            x  = int(input("Enter x : ")) 
            y  = int(input("Enter y : "))

            print(matrix[x][y])
        
        elif sel == "3":
            print("press any button to close")
            show_image(matrix)
            
        
    
            
    