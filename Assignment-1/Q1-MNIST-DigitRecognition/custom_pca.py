import numpy as np

class PCA:
    def __init__(self, numAxes):
        self.numAxes = numAxes
        self.principalAxes = None
    
    def calculateComponents(self, images):
        images = images - np.mean(images, axis=0)

        evals, evects = np.linalg.eig(np.cov(images.T))

        evects = evects.T
        sortedEvals = np.argsort(evals)[::-1]
        evals = evals[sortedEvals]
        evects = evects[sortedEvals]
        
        self.principalAxes = evects[0 : self.numAxes]

    def reduce(self, images):
        return np.dot(images, self.principalAxes.T)