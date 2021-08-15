import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def generate_dataset(num=1000, order=1, error=0.1, x_range=(0, 1000), y_range=(0, 1000), testing_split=False, split=(0.2)):
    """generates mock dataset based on specifications
    num = number of points
    x and y ranges are the range of each axis values the sample distribution will go to
    order is realted to polynomial order of values, e.g 1 = linear, 2 = curve
    error = fraction of each datapoint can be randomised error
    testing split returns two datasets of the same type for model testing
    split = the testing split fraction and only works if testing_split=True"""
    if order == 1:
        x = np.linspace(x_range[0], x_range[1], num)
        # generate y axis
        y = np.linspace(y_range[0], y_range[1], num)
        # create method for adding error
        multiplier = np.array([1, -1])
        x_noise = np.random.choice(multiplier, len(x))
        y_noise = np.random.choice(multiplier, len(y))
        #apply noise to axes
        x  = np.array([num + num*error*x_noise[idx] for idx, num in enumerate(x)]).reshape(1, -1)
        y  = np.array([num + num*error*y_noise[idx] for idx, num in enumerate(y)]).reshape(1, -1)
        #  form test and training data
        #  figure out how to randomly pick data points for testing and remove them from training data 
        data = np.concatenate((x, y))
        return data        



if __name__ == '__main__':
    data = generate_dataset(num = 100, error=0.1, x_range = (-50, 50), y_range=(1, 100))
    print(data.shape)
    fig = plt.figure()
    ax = plt.subplot()
    ax.scatter(data[0], data[1])
    plt.show()

# TODO fix error to account or size of each array value by changing to plus minus mean of array
# TODO think of different ways of generating line instead of linspace, that create more random values

    