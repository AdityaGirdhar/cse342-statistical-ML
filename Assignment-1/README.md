# Assignment 1
## Question 1: MNIST Digit Recognition
In this question, you’re going to use PCA to select the required subset of
features from MNIST and then perform classification on it.

a) Download the dataset from here:
https://www.kaggle.com/datasets/scolianni/mnistasjpg

b) Load the image dataset in your environment and convert it into a suitable
format for creating an ML model.

c) Implement PCA from scratch i.e. define your own PCA function or class for
it. You are not allowed to use ANY pre-built implementation from any
library. Note: Your implementation of PCA should be general, i.e., it can
work for any dataset.

d) Use kNN to train ML models on the training set of both original features
and the transformed features (number of PCs = 5, 25, 125) obtained from
PCA. Run the trained models on the test set and report the classification
accuracies.

e) Plot explained-variance (ratio of eigenvalue and sum of all eigenvalues) v/s
PCs. How many PCs do you need to select to cover at least 80% of the
variance? Do all this through programming.