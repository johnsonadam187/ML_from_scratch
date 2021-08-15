import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from basic_functions import generate_dataset

def most_basic_linreg(data, epochs=1000, learning_rate = 0.01):
    """Most basic form of linear regression, requires input of 2D np.array or list
    epochs = training cycles, learning rate is fraction of adjustment each epoch"""
    # get min and max of each axes for localising equation
    #start with random line equation get coef and y_int
    length = np.max(data.shape)
    m = np.random.uniform(-10, 10)
    b = np.random.uniform(-10, 10)
    # iterate the amount of epochs
    for num in range(0, epochs):
        #pick random point
        random_index = np.random.randint(0, length)
        x_point = data[0][random_index]
        y_point = data[1][random_index]
        #evaluate y_point and x_point
        y = m*x_point + b
        x = y_point - b
        #if y_point > y_line at x_point, increase y_intercept
        if y_point < y:
            b = b+learning_rate
        #elif y_point < y_line at x_point, decrease y_intercept
        elif y_point > y:
            b = b-learning_rate
        else:
            continue
        # if x_point > x_line at y_point, decrease slope
        if x_point < x:
            m = m+learning_rate
        # elif x_point < x_line at y_point, increase
        elif x_point > x:
            m = m-learning_rate
        else:
            continue
        # print(m, b)
        print(np.abs(x_point-x), np.abs(y_point - y))  


# TODO fix the equation 







if __name__ == '__main__':
    data = generate_dataset(num = 100, error=0.1, x_range = (1, 100), y_range=(1, 100))
    most_basic_linreg(data)