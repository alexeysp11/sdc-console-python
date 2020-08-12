# Let's try to build a neural network that can recognise
# digits
import numpy as np
import mnist
import matplotlib.pyplot as pt
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
##import pandas as pd
##from sklearn.tree import DecisionTreeClassifier

# Load the data set 
train_images = mnist.train_images()
train_labels = mnist.train_labels()
test_images = mnist.train_images()
test_labels = mnist.train_labels()

# Normalizing the images (pixel values from [0, 255] to
# [-0.5, 0.5] to make our network easier to train)
train_images = (train_images/255) - 0.5
test_images = (test_images/255) - 0.5

# Flatten each 28x28 image into a 784 dimensional vector
# to pass into the neural network
train_images = train_images.reshape((-1, 784))
test_images = test_images.reshape((-1, 784))

# Print the shape
print(train_images.shape)
print(test_images.shape)
