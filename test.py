import numpy as np
from PIL import Image
from math import sin,cos,radians

image=Image.open('input.jpg')
image_array=np.array(image)
height,width,_=image_array.shape
res=max(height,width)
transformed_array=np.full((res,res,_),255,np.uint8)

print("input.jpg is the input image and result.jpg is the output")
print("what transformation do you need to do:")
print("\t1. x_refelction") # horizontal rotation
print("\t2. y_refelction") # vertical rotation
print("\t3. clockwise_rotation")
a=input("Enter the choice: ")

if a=="1":
    transformed_matrix=np.array([[1,0],[0,-1]])
elif a=="2":
    transformed_matrix=np.array([[-1,0],[0,1]])
elif a=="3":
    angle=radians(float(input("Enter the angle you need to rotate: ")))
    transformed_matrix=np.array([[(cos(angle)),-sin(angle)],[sin(angle),cos(angle)]])
else:
    exit()
print("Processing....")

for y in range(1,height+1):
    for x in range(1,width+1):
        new_x,new_y=np.dot(transformed_matrix,[x,y])
        new_x=int(new_x)
        new_y=int(new_y)
        try:
            transformed_array[new_y][new_x]=image_array[y-1][x-1]
        except:
            pass
print("completed, output is at 'result.jpg'")
Image.fromarray(transformed_array).save("result.jpg")