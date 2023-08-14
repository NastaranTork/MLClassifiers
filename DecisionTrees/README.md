# Decision Tree Classifier
## Introduction
A decision tree is conceptually one of the simplest classifiers available but there are some key disadvantages that make it not a good choice for serious works.
For example: Overfitting, Unstable to small changes, Unstable to Noise, Non-Contiuous, Be biased in unbalanced classes, Greedy Algorithm.

## DataSet
For DataSet, I used **make-classification_ library** from sklearn.datasets. By using this library, you can generate a random n-class classification problem and get training data.

## Code Description
The first part of the code demonstrates the instability of the Decision Tree (DT) to minor changes in the data

x, y = make_classification(

    n_samples=1000,  # row number
    
    n_features=10, # feature numbers
    
    n_informative=6, # The number of informative features
    
    n_redundant = 2, # The number of redundant features
    
    n_repeated = 2, # The number of duplicated features
    
    n_classes = 2, # The number of classes 
    
    n_clusters_per_class=1,#The number of clusters per class
    
    random_state = 42 # random seed 
)

Using this function, I made two datasets for classification problems with slight changes in the number of informative features. 
Then DecisionTreeClassifier library provides a facility to train two decision tree classifiers for two data.

The following picture is the figure of the first tree:

![Figure of First Tree](https://media.github.umn.edu/user/27173/files/3501030b-8b1e-4c90-bf91-b1d29221e7c5)

And now you can see the figure of the second tree:

![Figure of Second Tree](https://media.github.umn.edu/user/27173/files/097c14f2-caf3-46e0-a33d-5e21bf44b40f)

You can realize that the slight change in features leads to create a different tree.

The second part provides an example of the DT's sensitivity to noise. I add some gaussian noise to the first, fifth, and tenth features of the first tree.

![Capture1](https://media.github.umn.edu/user/27173/files/6e6fb10d-d5b4-4c31-87c9-1e5818403582)

Now if you check the new fig of first tree and the previous one, you'll realize changes that happend because of the applied noise.

![Capture1](https://media.github.umn.edu/user/27173/files/d4fcf06b-6589-488a-ac95-8797a2320999)

## Visualization
plot_tree function is used to visually display (or plot) the structure of a decision tree. This can be especially useful for understanding the decision-making process of the tree, seeing how splits are made, and for presentation purposes.
