from scipy.stats import multivariate_normal
import numpy as np
from Entry import Entry


class CategoryClassifier:
    def __init__(self, labels, P0=None):
        self.n      = len(labels)
        self.labels = labels
        # n number of matrices. row = data instance, col = feature
        self.data   = [np.zeros((1,4)) for i in range(0, self.n)]
        self.P      = np.zeros(self.n)
        if P0 is None:
            self.P0 = np.ones(self.n) * 1/self.n
        else:
            self.P0 = P0

    def __extract_features(self, d):
        day = d.date.day 
        val = d.val 
        key_array = d.targetName.encode()
        keyval = sum(key_array)
        nkey = len(key_array)
        return [day, val, keyval, nkey]

    def __fx(self, x):
        pass

    def train(self, data, label):
        if type(data) is type(Entry):
            f = np.array(self.__extract_features(data))
            self.data[label] = np.vstack(( self.data[label], f ))

        elif type(data) is type(list):
            for ii, entry in enumerate(data):
                f = np.array(self.__extract_features(entry))
                label_ii = label[ii]
                self.data[label_ii] = np.vstack(( self.data[label_ii], f ))
        
        for ii in range(0, self.n):
            data_ii = self.data[ii]
            m = np.mean(data_ii, axis=0)
            c = np.cov(data_ii.T)
            self.P[ii] = multivariate_normal(mean=m, cov=c)

    def classify(self, D):
        pass

