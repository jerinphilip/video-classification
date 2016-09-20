import numpy as np
from parser import create_parser
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import matplotlib.colors
from sklearn.cluster import KMeans
from functools import partial, reduce
from extract import read_trackers


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    # Extract data.
    data = read_trackers(args.descriptors)
    
    



