# Introduction
Random Forest is made out of decision trees and not only has the simplification feature of the decision tree but also fixes the overfitting problem. Let's learn its process.

**Step 1:** Bootstrapped Datasets => Randomly choose samples from your original data. Also, you can choose one sample more than once.

**Step 2:** Features => Randomly select subsets of features for each created dataset

**Step 3:** Decision Trees => Build DT for each subset of features and dataset

**Step 4:** Prediction => At the test level, you should apply the new sample to all decision trees and then combine their results. For example, in classification problem, you can take the mejority voting to combine results or for regression problem, you can average the results.

## Notes
__As a result, the whole point of thr random forest is bootstap + aggregating = bagging. Bootstapping makes new data for each random tree and using subset of features leads to correlation between trees.

__log n^2 (n is the total number of features) can be a good idea for number of features for each tree.
