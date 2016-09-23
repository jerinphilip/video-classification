import numpy as np
from numpy.linalg import norm
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from functools import partial

# project : descriptor, basis -> histogram
def project(basis, descriptor):
    return np.dot(basis, descriptor)

# generate_BagOfWords : [descriptors] -> Int -> [visual_words]
def generate_BagOfWords(data, count=4096):
    print(data)
    K = KMeans(n_clusters=count)
    K.fit(data)
    #print("Generating cluster centers", K.cluster_centers_)
    return np.array(K.cluster_centers_)

def generate_histograms(sample, words):
    # For each entry in data, project it onto the words basis
    # get a histogram representation
    project_basis = partial(project, words)
    contributions = np.array(list(map(project_basis, sample)))
    transformed = np.sum(contributions, axis=0)
    return transformed


