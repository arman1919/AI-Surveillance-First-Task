# # չգիտեի  գրադարան որ  ստացված մատրիցը ցույց տար
# # numpy  սովորել եմ lab ից
# # validatia ն արած չի

# import numpy as np
# import matplotlib.pyplot as plt



# def random_color(size):
#     return np.random.randint(0, 256, size=size + [3])  


# def show_image(matrix):
#     plt.imshow(matrix)
#     plt.show(block=False)  
#     plt.waitforbuttonpress()


# if __name__ ==  "__main__":
#     matrix = random_color([10000,10000])
 
#     while True:
       
#         print("1) Change the RGB pixel values in the image coordinates (x, y)")
#         print("2) Get the RGB pixel values in the image coordinates (x, y)")
#         print("3) Show the image by printing the pixel color values of the image")
#         sel = input("Select option :")
        
#         if sel == "1":
#             x  = int(input("Enter x : ")) 
#             y  = int(input("Enter y : "))

#             R = int(input("Enter cllor  R:"))
#             G = int(input("Enter cllor  G:"))
#             B = int(input("Enter cllor  B:"))
            
#             matrix[x][y] = [R,G,B]
        
#         elif sel == "2":
#             x  = int(input("Enter x : ")) 
#             y  = int(input("Enter y : "))

#             print(matrix[x][y])
        
#         elif sel == "3":
#             print("press any button to close")
#             show_image(matrix)
            
#-------------------------------------------------------------------------------------------------



import random
import matplotlib.pyplot as plt

class image:
    def __init__(self,row,col):
        self.pixels  = []
        
        for _ in range(row):
            self.pixels.append([])
        
        for i in self.pixels:
            for j in range(col):
                
                i.append(random.randint(1,256))
            
            
    def set_pixel(self,x,y,new_pixel):
        self.pixels[x][y] = new_pixel
    
    def  get_pixel(self,x,y):
        return self.pixels[x][y]
    
    def show_image(self):
        plt.imshow(self.pixels)
        plt.show(block=False)  
        plt.waitforbuttonpress()
        
        


img = image(10,10)

print(img.get_pixel(5,5))

img.set_pixel(5,5,165)

print(img.get_pixel(5,5))

img.show_image()
