# Introduction
Support Vector Machines (SVM) serve as a sophisticated technique for clustering and classifying data in high-dimensional spaces. However, traditional SVM has its limitations. Specifically, it assumes that the data is linearly separable and is inherently a binary classifier. Additionally, it does not provide continuous-valued confidence scores to gauge the strength of its classifications. 
### Objective of SVM
The primary objective of SVM is to discover the optimal hyperplane that not only separates the dataset but also maximizes the margin between different classes.
### Types of Margins
SVM utilizes two types of margins for classification: Hard Margin and Soft Margin.
#### Hard margin:
In Hard Margin SVM, the training model aims to find the parameters w and b that satisfy the equation w⋅x+b=0.
#### Soft margin: 
Soft Margin SVM introduces a penalty for data points that fall on the incorrect side of the margin, making the model more flexible in handling outliers or noisy data.

### Kernel SVM: 
For datasets that are not linearly separable, traditional SVM techniques fall short. The solution involves mapping the data to a different space using a mapping function, Φ, where a linear decision boundary can be identified. Interestingly, there is no need to compute this mapping directly. Instead, one can focus on the kernel function Kernel Func=Φ(x)⋅Φ(y). Popular kernel functions include Polynomial, Gaussian, and Sigmoid kernels.

### Example: 
To show the function of the SVM classification, I implement a function that produces fake data based on the given k (number of classes) and N (number of data points).




