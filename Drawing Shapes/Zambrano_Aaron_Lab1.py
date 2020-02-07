# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:01:47 2020

Course: CS 2302 Data Structures

@author: Aaron Zambrano

Assignment: Lab 1 - Recursion

Instructor: Dr. Olac Fuentes

T.A: Oscar Galindo

Last Modified on Mon Jan 31 9:53 PM 2020

Purpose of the program is to draw figures assigned using recursive methods
and utilizing the matplotlib library to generate plots to draw and demostrate the practice of
recursion. 

"""
import numpy as np
import matplotlib.pyplot as plt
import math

'''Returns the coordinates of the points in a circle given center and radius
    Parameters
    ----------
    center: list
        The coordinates for the center of the circle
    rad: int
        The size of the radius of the circle
    Returns
    -------
    float
        The coordinates of the x and y points in a circle
    Assumptions: Center and Radius can be of any size n including floating points numbers
'''
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    # Parametric Equiation of a circle for x coordiantes of the points
    x = center[0]+rad*np.sin(t) 
    # Parametric Equiation of a circle for y coordiantes of the point
    y = center[1]+rad*np.cos(t) 
    return x,y

''' Plots the inner circles of the desired figures
    Parameters
    ----------
    ax: subplot
        Contains the subplot of the desired shape
    n: int
        Recursion iteration to draw the desired shape
    center: list
        The coordinates for the center of the circle
    rad: int
        The size of the radius of the circle 
    Returns
    -------
        None
    Assumptions: A center and radius can be of any size 
'''
def draw_inner_circles(ax,n,center,radius):
    if  n > 0:
        x,y = circle(center,radius)
        ax.plot(x,y,linewidth=0.5,color = 'k')
        draw_inner_circles(ax, n-1, center, abs(radius - n))
    return

''' Draws traingles given coordiantes of the triangle and each coordiantes individually
    Parameters
    ----------
    ax: subplot
        Contains the subplot of the desired shape
    n: int
        Recursion iteration to draw the desired shape  
    tri: 2D numpy array
        The coordinates to construct the triangle
    p1: int
         Bottom-left point of the triangle
    p2: int
         Top point of the triangle
    p3: int
         Bottom-right point of the triangle
    p4: int
         Coordinate of the first point of the triangle
    Returns
    -------
    None
    Assumptions: A 4x2 numpy array that makes a triangle shape 
'''
def draw_triangles(ax,n,tri,p1,p2,p3,p4):
    if n > 0:
     ax.plot(tri[:,0],tri[:,1],linewidth=0.5,color = 'k')   
     #Calculatring midpoints of each side of a triangle
     p1 = midpoint(p1,p2)
     p2 = midpoint(p2,p3) 
     p3 = midpoint(p3,p4) 
     p4 = p1
     # Update coordinates of the triangle         
     tri = np.array([p1,p2,p3,p4])
     draw_triangles(ax,n-1,tri,p1,p2,p3,p4)
     return
 
''' Draws triangles within the orignal triangle in a grid-fashion way given the triangle coordinates
    Parameters
    ----------
    ax: subplot
        Contains the subplot of the desired shape
    n: int
        Recursion iteration to draw the desired shape 
    tri: 2D numpy array
        The coordinates to draw a triangle  
    Returns
    -------
    None
    Assumptions: A 4x2 numpy array that makes a triangle shape
'''
def draw_grid_triangles(ax,n,tri):
    if n > 0:
        ax.plot(tri[:,0],tri[:,1],linewidth=0.5,color = 'k') 
        # Coordinates of midpoint of left side of the triangle
        m1 = midpoint(tri[0],tri[1]) 
        # Coordinates of the midpoint of right side of the triangle
        m2 = midpoint(tri[1],tri[2]) 
        # Coordinates of the midpoint of the base of the triangle
        m3 = midpoint(tri[2],tri[3])  
        # drawing triangles given the coordinates that are relative to the original triangle
        draw_grid_triangles(ax,n-1,np.array([m1,m2,m3,m1]))
        draw_grid_triangles(ax,n-1,np.array([tri[0],m1,m3,tri[0]]))
        draw_grid_triangles(ax,n-1,np.array([m1,tri[1],m2,m1]))
        draw_grid_triangles(ax,n-1,np.array([m3,m2,tri[2],m3]))
    return

''' Calculates the midpoint of a line given the start and end points
    Parameters
    ----------
    ax: subplot
        Contains the subplot of the desired shape
    n: int
        Recursion iteration to draw the desired shape  
    p1: list
        Start point of a line
    p2: list
        End point of a line
    Returns
    -------
    mid: list
        coordinates of the midpoint of a line
    Assumptions: Points must be a list of size 2
'''
def midpoint(p1,p2):
    mid = [(p1[0]+p2[0])*0.5 , (p1[1]+p2[1])*0.5]
    return mid

''' Draws a square with one square in each corner of the original given the coordiantes and the center of a square
    Parameters
    ----------
    ax: subplot
        Contains the subplot of the desired shape
    n: int
        Recursion iteration to draw the desired shape
    square: 2D numpy array
        The coordinates to draw a square 
    center: list
        The coordinates of the center of a square
    Returns
    -------
    None
    Assumptions: A 4x2 numpy array that makes a square shape any coordinates as the center
'''
def draw_squares(ax,n,square,center):
    if n > 0:
        #Calculating the corner points of a square
        square = get_points(square,center)
        ax.plot(square[:,0],square[:,1],linewidth=0.5,color = 'k')
        # Bottom-Left Square
        draw_squares(ax,n-1,square*0.5,square[0])
        # Top-Right Square
        draw_squares(ax,n-1,square*0.5,square[1])
        # Top-Left Square
        draw_squares(ax,n-1,square*0.5,square[2])
        # Bottom-Left Square
        draw_squares(ax,n-1,square*0.5,square[3])  
    return

''' Calculates the corner point of a square given a center
    Parameters
    ----------
    square: 2D numpy array
        The cooridates of a square 
    c: list
        The coordinates of the center of a square
    Returns
    -------
    2D numpy array 
        The coordinates to shape a square with dimensions 5x2
    Assumptions: Coordinates of a square will be calculate if a 2D array of size 5x2 
    is given as well as a list of size 2 
'''
def get_points(square,c):
    p1 = square[0]
    p2 = square[1]
    # Length of one side of a square
    L = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 )
    return np.array([[c[0]-L/2,c[1]-L/2],[c[0]-L/2,c[1]+L/2],[c[0]+L/2,c[1]+L/2],[c[0]+L/2,c[1]-L/2],[c[0]-L/2,c[1]-L/2]])

''' Draws a tree given the x and y coodintates of a point,the change of x, and the change of y
    Parameters
    ----------
    ax: subplot
        Contains the subplot of the desired shape
    n: int
        Recursion iteration to draw the desired shape
    x0: int
        x coordiante of a point
    y0: int
        y coordiante of a point
    dX: int
        Change of x of the x coordinate
    dY: int
        Change of y of the y coordinate    
    Returns
    -------
    None
    Assumptions: x0,y0,dX,dY can be either integer or floating point  
'''
def draw_trees(ax,n,x0,y0,dX,dY):
    if n>0:
        # Coordinates of a line for left and right side of tree
        l1 = np.array([[x0,y0],[x0-dX,y0*1.8-dY]])
        l2 = np.array([[x0,y0],[x0+dX,y0*1.8-dY]])
        
        ax.plot(l1[:,0],l1[:,1],linewidth=0.5,color = 'k')
        ax.plot(l2[:,0],l2[:,1],linewidth=0.5,color = 'k')
        # left side
        draw_trees(ax,n-1,x0-dX,y0*1.8 - dY,dX/2,dY - 150)
        # right side
        draw_trees(ax,n-1,x0+dX,y0*1.8 - dY,dX/2,dY - 150)
    return

''' Draws branches given a 1x2 numpy array as a starting point, the length of a line, the degree of an angle, 
    and the change of degree
    Parameters
    ----------
    ax: subplot
        Contains the subplot of the desired shape
    n: int
        Recursion iteration to draw the desired shape  
    start: 2D numpy array
        The coordinates of a point where a line begans
    L: int
        Length of a line
    degree: int
        Angle of a line in degrees 
    new_degree:
        Updated angle of a line in degrees
    Returns
    -------
    None
    Assumptions: Starting point must be a 2D numpy array of with dimensions 1x2. The tree can be drawn at different
    directions depending on the degree.
'''
def draw_branches(ax,n,start,L,degree,new_degree):
    
    plt.grid()
    # change of y coordinate for next point
    y0 = np.sin(math.radians(degree)) 
    # change of x coordinate for next point
    x0 = np.cos(math.radians(degree))
    # Calculating end point   
    end = start + L*np.array([[x0,y0]])
    # new coordinates for next line
    start = np.append(start,end,axis=0)
    ax.plot(start[:,0],start[:,1],linewidth=0.5,color = 'k')
    if n > 0 :
        
        #left side of branch
        draw_branches(ax,n-1,end,L/1.12,degree + new_degree/1.9,new_degree/1.5)
        #right side of branch
        draw_branches(ax,n-1,end,L/1.12,degree - new_degree/1.9,new_degree/1.5)  
    return

if __name__ == "__main__":
    plt.close('all')
    '''
    Circles
    '''
#    fig, ax = plt.subplots()
#    draw_inner_circles(ax,3,[0,0],10)
#    ax.set_aspect(1.0)
#    ax.axis()
#    plt.show()
#    
#    fig, ax2 = plt.subplots()
#    draw_inner_circles(ax2,6,[0,0],40)
#    ax2.set_aspect(1.0)
#    ax2.axis()
#    plt.show()
#    
#    fig, ax3 = plt.subplots()
#    draw_inner_circles(ax3,9,[0,0],90)
#    ax3.set_aspect(1.0)
#    ax3.axis()
#    plt.show()
    
    '''
    Triangles
    '''
    orig_size = 500
#    # Coordinates of a Triangle
    tri1 = np.array([[0,0],[orig_size/2,orig_size],[orig_size,0],[0,0]]) 
#   
#    fig, ax4 = plt.subplots()
#    draw_triangles(ax4,3,tri1,tri1[0],tri1[1],tri1[2],tri1[3])
#    ax4.set_aspect(1.0)
#    ax4.axis()
#    plt.show()
#    
#    fig, ax5 = plt.subplots()
#    draw_triangles(ax5,6,tri1,tri1[0],tri1[1],tri1[2],tri1[3])
#    ax5.set_aspect(1.0)
#    ax5.axis()
#    plt.show()
#    
#    fig, ax6 = plt.subplots()
#    draw_triangles(ax6,9,tri1,tri1[0],tri1[1],tri1[2],tri1[3])
#    ax6.set_aspect(1.0)
#    ax6.axis()
#    plt.show()

    '''
    Grid triangles
    '''
#    fig, ax7 = plt.subplots()
#    draw_grid_triangles(ax7,1,tri1)
#    ax7.set_aspect(1.0)
#    ax7.axis()
#    plt.show()
#    
#    fig, ax8 = plt.subplots()
#    draw_grid_triangles(ax8,2,tri1)
#    ax8.set_aspect(1.0)
#    ax8.axis()
#    plt.show()
#    
#    fig, ax9 = plt.subplots()
#    draw_grid_triangles(ax9,3,tri1)
#    ax9.set_aspect(1.0)
#    ax9.axis()
#    plt.show()
#    
    
    '''
    Squares
    '''
    # Coordintates of a square
    sq = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
    
    fig, ax11 = plt.subplots()
    draw_squares(ax11,2,sq,[0,0])
    ax11.set_aspect(1.0)
    ax11.axis()
    plt.show()
    
    fig, ax12 = plt.subplots()
    draw_squares(ax12,3,sq,[0,0])
    ax12.set_aspect(1.0)
    ax12.axis()
    plt.show()
    
    fig, ax10 = plt.subplots()
    draw_squares(ax10,4,sq,[0,0])
    ax10.set_aspect(1.0)
    ax10.axis()
    plt.show()
    
    
    
    '''
    Trees
    '''
    fig, ax13 = plt.subplots()
    draw_trees(ax13,4,500,1000,1000,1000)
    ax13.set_aspect(1.0)
    ax13.axis()
    plt.show()
    
    fig, ax14 = plt.subplots()
    draw_trees(ax14,5,500,1000,1000,1000)
    ax14.set_aspect(1.0)
    ax14.axis()
    plt.show()
    
    fig, ax14 = plt.subplots()
    draw_trees(ax14,6,500,1000,1000,1000)
    ax14.set_aspect(1.0)
    ax14.axis()
    plt.show()
    

    
    
    '''
    Branches
    '''
    # starting point of a line
    original = np.array([[0,0]])
    degree = 90
    
    fig, ax16 = plt.subplots()
    draw_branches(ax16,2,original,10,degree,degree)
    ax16.set_aspect(1.0)
    ax16.axis()
    plt.show()
    
    fig, ax17 = plt.subplots()
    draw_branches(ax17,4,original,10,degree,degree)
    ax17.set_aspect(1.0)
    ax17.axis()
    plt.show()
    
    fig, ax18 = plt.subplots()
    draw_branches(ax18,8,original,10,degree,degree)
    ax18.set_aspect(1.0)
    ax18.axis()
    plt.show()
#    
#
#    
    
    
    
    
    
    
    
    
    
    
    

    

    
 
    
  
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    