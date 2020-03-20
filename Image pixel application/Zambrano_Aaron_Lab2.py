# -*- coding: utf-8 -*-
"""
Created on Tues Feb 4 9:54 2020

Course: CS 2302 Data Structures

@author: Aaron Zambrano

Assignment: Lab 2 - Algorithm Analysis

Instructor: Dr. Olac Fuentes

T.A: Oscar Galindo

Last Modified on Thur Feb 14 10:36 AM 2020

Purpose of the program is to find the brightest pixel and areas of a MxN image from HxW regions and display those areas
in the image to analyze the different time complexities of the same algorithm to find those regions.
"""
import numpy as np
import matplotlib.pyplot as plt
import os

# Reads image in directory and returns color and gray-level images
def read_image(imagefile):

    img = (plt.imread(imagefile)*255).astype(int)
    img = img[:,:,:3]  # Remove transparency channel
    img_gl = np.mean(img,axis=2).astype(int) #Converts pixel values into integers

    return img, img_gl

'''Draws a colored rectangle given the height, width, and upper-left corner (r,c)'''
def draw_in_image(I,r,c,h,w,clr):
    #coordinates to draw a square
    r = np.array([r,r+w,r+w,r,r])
    c = np.array([c,c,c+h,c+h,c])
    
    I.plot(r,c,linewidth=1.5,color = clr)
    return

'''Return the coordinates of the brightest pixel given grey-scale image
   Assumption: Collision can occur when finding the max pixel value '''
def brightest_pixel(ax,I): 
    h = w = 1
    pixel_max = pixel_value = 0
    
    #x is columns y is rows
    x = y = 0
    #Transversing through image
    for i in range(len(I)):
        for j in range(len(I[i])):

            pixel_value = I[i][j]
            
            #Pixel Coordinates
            if pixel_value > pixel_max:
                pixel_max = pixel_value
                y,x = i,j
            else:
                continue
    print('Coordinates: ', x,y)
    print('Value: ',I[y][x])
    
    
    #Top right coordinates of the pixel to start to draw
    r= x-w * 0.5
    c= y-h * 0.5
    
    draw_in_image(ax,r,c,h,w,'c') 
    return

     
#v.1.1
'''Returns the upper-left corner point of the region with the maximum sum given the axis, a grey-scale image,
   height and width of a region
   Assumption: Algorithm is expected to run the slowest''' 
def naive_algorithm_1(ax,grey_img,h,w):
    x = y = 0
    r = c = 0
    max_sum = sum_value = 0
    for row in range(0,len(grey_img) - h + 1):
        
        for col in range(0,len(grey_img) - w + 1):
            
            for height in range(0,h):
   
                for width in range(0,w):
                           
                    sum_value += grey_img[row + height][col + width]

            if sum_value > max_sum: 
                max_sum = sum_value

                y,x = row,col
            sum_value = 0

            
    #Top right coordinates of the rectangle
    r= x
    c= y
    draw_in_image(ax,r,c,h,w,'b')
                 
    return r,c

#v 1.2
'''Returns the upper-left corner point of the region with the maximum sum given the axis, a grey-scale image,
   height and width of the region
   Assumption: Algorithm is expected to run a bit faster than the first version''' 
def naive_algorithm_2(ax,grey_img,h,w):  
    x = y = 0
    r = c = 0
    max_sum = sum_value = 0
    for row in range(0,len(grey_img) - h):
        
        for col in range(0,len(grey_img) - w):
            
            sum_value = np.sum(grey_img[row : row+h ,col : col+w])
            #getting max sum of region
            if sum_value > max_sum: 
                max_sum = sum_value
                
                y,x = row,col
       
    #Top right coordinates of the rectangle
    r= x
    c= y
    draw_in_image(ax,r,c,h,w,'r')
                 
    return r,c
      
#v.2.1
'''Returns the upper-left corner point of the region with the maximum sum given the axis, a grey-scale image,
   height and width of the region
   Assumption: Algorithm is expected run faster than the naive algorithm solutions''' 
def integral_image_algorithm_1(ax,I,h,w):
    
    #Computing the Integral image
    integral = np.cumsum(I,1)
    integral = np.cumsum(integral,0)
    integral = np.insert(integral,0,0,0)
    integral = np.insert(integral,0,0,1)
    
    x = y = 0
    r = c = 0
    
    sum_value = max_sum = 0
    # Computes the sum of pixels of the region of interest 
    for row in range(0,len(integral) - h):
        
        for col in range(0,len(integral[0]) - w):
             
            #bottom-right - bottom-left - upper-left + upper right
            sum_value = integral[row + h][col + w]  - integral[row + h][col] - integral[row][col + w] + integral[row][col]
            
            #getting max sum of region
            if sum_value > max_sum: 
                max_sum = sum_value
                y,x = row,col        
    r= x
    c= y
    draw_in_image(ax,r,c,h,w,'m')
    
    return r,c
    
#v.2.2
'''Returns the upper-left corner point of the region with the maximum sum given the axis, a grey-scale image,
   height and width of the region
   Assumption: Algorithm is expected to run the fastest''' 
def integral_image_algorithm_2(ax,I,h,w):
    
    x = y = 0
    
    integral = np.cumsum(I,1)
    integral = np.cumsum(integral,0)
    integral = np.insert(integral,0,0,0)
    integral = np.insert(integral,0,0,1)
    
    A = integral[:len(integral)-h,:len(integral[0])-w]

    B = integral[:len(integral)-h, w:]
    
    C = integral[h:,:len(integral[0])-w]
    
    D = integral[h:,w:]
    
    #All the sums of each regions contain in an 2D array
    sum_value = D-B-C+A
    
    # max sum of region
    max_value = np.max(sum_value)
    # location where the max value is at from sum_value
    index_from_sum = np.argwhere(sum_value[:]==max_value)
    # upper-right value of the region from all possible upper right regions
    value_a = A[index_from_sum[0][0]][index_from_sum[0][1]]
    # location where upper-right value is at from the Integral Image
    index_from_integral = np.argwhere(integral[:]==value_a)
    
    # location of the upper-right value in Integral image is the same location from the orignal image
    y,x = index_from_integral[0][0],index_from_integral[0][1]
    
    r,c = x,y
    
    draw_in_image(ax,r,c,h,w,'b')

    return r,c   

'''Return the size of the region given the user input of a height and width
    Assumption: Take in the case if the height and width of the region exceed the image size '''
def pick_size(img_gl,h,w):
    h = int(input('Please enter a height: '))
    w = int(input('Please enter a width : '))
    if h > len(img_gl) or w > len(img_gl[0]):
        print('Height or Width exceed image size')
        return
    return h,w

'''Reads a file from an image directory and returns the colored and grey-scaled images along with the figures and axes
    Assumption: files must be .png images'''
def read_file(file,img_dir):
    print(file)
    if file[-4:] == '.png': # File contains an image
        img, img_gl = read_image(img_dir+file)
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    return img, img_gl, fig, ax1, ax2

'''Displays menu to select options given the image files and image directory
    Assumption: files must be .png images'''
def menu(img_files,img_dir):
    h = w = 0
    plt.close('all')
    
    #Select a png file from directory
    print('1 to %d' %(len(img_files)),end='')
    num = int(input('Hello, Please select an image from the range above: '))
    
    #Checks if the file exist
    if num <= 0 or num > len(img_files):
        print('No image found')
        return
    
    select_image = img_files[num-1]
    img,img_gl,fig,ax1,ax2 = read_file(select_image,img_dir)
    
    print('1 Find brightest pixel in image')
    print('2 Find brightest region using naive algorithm 1')
    print('3 Find brightest region using naive algorithm 2')
    print('4 Find brightest region using the Integral Image algorithm 1')
    print('5 Find brightest region using the Integral Image algorithm 2')
    
    option = int(input('Please select a choice (1-5): '))
    
    if option == 1:
        brightest_pixel(ax1,img_gl)
    if option == 2:
        h,w = pick_size(img_gl,h,w)
        print('Region coordinates: ',naive_algorithm_1(ax1,img_gl,h,w))
    if option == 3:
        h,w = pick_size(img_gl,h,w)
        print('Region coordinates: ',naive_algorithm_2(ax1,img_gl,h,w))
    if option == 4:
        h,w = pick_size(img_gl,h,w)
        print('Region coordinates: ',integral_image_algorithm_1(ax1,img_gl,h,w))
    if option == 5:
        h,w = pick_size(img_gl,h,w)
        print('Region coordinates: ',integral_image_algorithm_2(ax1,img_gl,h,w))
    ax1.imshow(img)                  #Display color image
            
    ax2.imshow(img_gl,cmap='gray')   #Display gray-level image
    plt.show()

    return 
    
if __name__ == "__main__":
    # Directory where images are stored
    img_dir = '.\\solar images\\'

    img_files = os.listdir(img_dir)  # List of files in directory

    menu(img_files,img_dir)


            
    
            
            