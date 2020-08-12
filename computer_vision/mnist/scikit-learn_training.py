import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
# Load data
iris = load_iris()
plt.figure(figsize=((20,13)))
clf = DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
plot_tree(clf, 
          filled=True, 
          feature_names=iris.feature_names, 
          class_names=iris.target_names, 
          rounded=True)
plt.show()
