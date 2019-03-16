'''
author: vladdtuz 
date: 16/03/2019
version: 1

Python script to determine and plot Morh's circle of principle stresses

'''
import math 
import matplotlib.pyplot as plt
def principleStress (x,y,tau):
    '''
    Function to determine principle stress from element stresses
    Input : 
        X - stress in x direction
        Y - stress in y direction
        tau - shear stress xy
    Output:
        stress 1 - principle stress in direction 1
        stress 2 - principle stress in direction 2
        radius - maximum shear stress
    '''
    center = (x+y)/2
    radius = math.sqrt(pow(((x-y)/2),2)+math.pow(tau,2))
    stress1 = center + radius
    stress2 = center - radius
    angle1 = math.degrees(math.atan((2*tau)/(x-y)))/2
    return stress1, stress2, radius, angle1

def orientation(x,y,tau,angle):
    '''
    Function to determine stress rotated about an angle
    Input :
        x - stress in x direction
        y - stress in y direction
        tau - shear stress xy
        angle - angle to rotate
    Output:
        dir x - new, rotated stress in x direction
        dir y - new, rotated stress in y direction
        ta - new, rotated shear stress
    '''
    dir_x = (x+y)/2 + (x-y)/2*math.cos(math.radians(2*angle))+tau*math.sin(math.radians(2*angle))
    dir_y = (x+y)/2 - (x-y)/2*math.cos(math.radians(2*angle))+tau*math.sin(math.radians(2*angle))
    ta = -(x-y)/2*math.sin(math.radians(2*angle)) + tau*math.cos(math.radians(2*angle))
    return dir_x,dir_y,ta

def circle(x,y,tau):
    '''
    Function to plot Mohr's circle based 
    Input:
        x - stress in x direction
        y - stress in y direction
        tau - shear stress xy
    Output:
        plot- Mohr's circle
    '''
    x_data = []
    y_data = []
    for i in range(0,181):
        x_data.append(orientation(x,y,tau,i)[0])
        y_data.append(orientation(x,y,tau,i)[2])

    plt.plot(x_data,y_data)
    plt.ylabel('Shear stress')
    plt.xlabel('Stress in direction x')
    plt.title('Mohr Circle of element')
    plt.grid(True)
    plt.show()
    return None
