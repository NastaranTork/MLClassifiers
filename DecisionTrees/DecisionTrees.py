import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt


# First Class
x1, y1 = make_classification(

    n_samples=1000,  # row number
    
    n_features=10, # feature numbers
    
    n_informative=4, # The number of informative features
    
    n_redundant = 2, # The number of redundant features
    
    n_repeated = 2, # The number of duplicated features
    
    n_classes = 2, # The number of classes 
    
    n_clusters_per_class=1,#The number of clusters per class
    
    random_state = 42 # random seed 
)

# Second Class
x2, y2 = make_classification(

    n_samples=1000,  # row number
    
    n_features=10, # feature numbers
    
    n_informative=3, # The number of informative features
    
    n_redundant = 2, # The number of redundant features
    
    n_repeated = 2, # The number of duplicated features
    
    n_classes = 2, # The number of classes 
    
    n_clusters_per_class=1,#The number of clusters per class
    
    random_state = 42 # random seed 
)

# Training Data 
m1 = DecisionTreeClassifier(max_depth= 3)
m1.fit(x1,y1)

m2 = DecisionTreeClassifier(max_depth= 3)
m2.fit(x2, y2)

#Plot first tree
fig = plt.figure(figsize=(12,6))  # To change the size of image
fig2 = plot_tree (m1, filled= True, fontsize= 10)

#Plot first tree
fig3 = plt.figure(figsize=(12,6))  # To change the size of image
fig4 = plot_tree (m2, filled= True, fontsize= 10)

#Adding noise
X1_Copy = np.copy(x1)
X1_Copy[:,[0,5,9]] *= np.random.normal(size=(x1.shape[0],3))
plt.boxplot(X1_Copy)

# Training Data with Guassian Noise
m3 = DecisionTreeClassifier(max_depth=3)
m3.fit(X1_Copy, y1)
fig = plt.figure(figsize=(12,6))
figure5 = plot_tree(m3, filled= True, fontsize=10)
