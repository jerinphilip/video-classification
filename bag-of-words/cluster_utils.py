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
    return K


def generate_histograms(sample, K):
    # For each entry in data, project it onto the words basis
    # get a histogram representation
    #project_basis = partial(project, words)
    get_cluster = lambda x: K.predict(x)
    contributions = np.array(list(map(get_cluster, sample)))
    #transformed = np.sum(contributions, axis=0)
    transformed = np.histogram(contributions, bins=range(len(K.cluster_centers_)))
    print(transformed)
    return transformed
