# Introduction
Random Forest is made out of decision trees and not only has the simplification feature of the decision tree but also fixes the overfitting problem. Let's learn its process.

**Step 1:** Bootstrapped Datasets => Randomly choose samples from your original data. Also, you can choose one sample more than once.

**Step 2:** Features => Randomly select subsets of features for each created dataset

**Step 3:** Decision Trees => Build DT for each subset of features and dataset

**Step 4:** Prediction => At the test level, you should apply the new sample to all decision trees and then combine their results. For example, in classification problem, you can take the mejority voting to combine results or for regression problem, you can average the results.

## Notes
__As a result, the whole point of thr random forest is bootstap + aggregating = bagging. Bootstapping makes new data for each random tree and using subset of features leads to correlation between trees.

__log n^2 (n is the total number of features) can be a good idea for number of features for each tree.

## Implementation
**I) Data Evaluation:** Depends on the data and concept of the project, you can use different ways to evaluate your data but some tricks are general like: data.shape, data.describe() [for quick summary statistics], plot.

**II) Data Preparation:** 
      __One-Hot Encoding: Converting categorical features to numerical ones without an arbitrary ordering.
      
      __Features and Target: Specifying the feature that you wanna predict and removing it from your data
      
      __Trainnig and Testing: Splitting your data
      
      __Baseline: a maximum error that you hope to decrease it by prediction ability if your model
      
**III) Training Data:** In this step, you just need to import the model that you wanna use (here we used Random Forest). Then you have to define your model parameters and in random forest, I just needed to define the number of decision trees

**IV) Testing Model:**  Calculate the error of your model by using testing data

