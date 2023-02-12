import numpy as np

class PCA:
    def __init__(self, num_pcs):
        self.num_pcs = num_pcs
        self.pcs = None
        self.mean = None
        
    def fit(self, X):
        # Adjusting our data relative to the mean
        self.mean = np.mean(X, axis=0)
        X = X - self.mean
        
        # Generating the covariance matrix (we transpose our data matrix for easier calculations)
        cov = np.cov(X.T)
        
        # Generating eigenvectors and eigenvalues
        eigvectors, eigvalues = np.linalg.eig(cov)
        eigvectors = eigvectors.T
        
        # Sorting the eigenvectors according to eigenvalues
        idxs = np.argsort(eigvalues)[::-1]
        eigvalues = eigvalues[idxs]
        eigvectors = eigvectors[idxs]
        
        # Storing the first n principal components
        self.pcs = eigvectors[0:self.num_pcs]
    
    def transform(self, X):
        X = X - self.mean
        return np.dot(X, self.pcs.T)