import random #This is the class that helps us to generate the random numbers
import math
def calculatePi(num):
    '''
    This is a function that takes in a number to be iterated through, giving points to then use calculate the value of pi
    '''
    assert type(num) == int and 0 < num < 1000000000, 'The value of num should be greater than zero and it must be an integer'
    
    graphPoints = []
    inside_the_circle = 0
    outside_the_circle = 0
    for i in range(num):
        x = round(random.random(), 1) #the round method is used to round the decimal to one decimal place
        y = round(random.random(), 1)
        newPoint = {'x':x, 'y':y}
        graphPoints.append(newPoint)
    for n in graphPoints:
        distance = ((n['x'])**2) + ((n['y'])**2)
        if distance <= 1:
            inside_the_circle += 1
        else:
            outside_the_circle += 1
    pi = ( 4 * inside_the_circle) / num

    return pi
