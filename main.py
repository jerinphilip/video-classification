from parser import create_parser
#from matplotlib import pyplot as plt
#import matplotlib.colors
from functools import partial, reduce
import bow.dataset_utils as du
from operator import add
import bow.cluster_utils as cu
import numpy as np



if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    np.random.seed(42)

    cluster_size = 4096

    # Extract data.
    print("Reading data...",)
    #data = du.read_data(args.metafile, args.descriptor, 0.1)
    data = du.read_data(args.metafile, args.descriptor, 1)
    print("Done.")
    _class, descriptors = zip(*data)

    print("Squeezing...",)
    descriptors_flattened = np.array(reduce(add, descriptors))
    print("Done")

    # Generate K Means
    print("Computing KMeans...",)
    K = cu.generate_BagOfWords(descriptors_flattened, cluster_size)
    print("Done")

    print("Writing out cluster centers...",)
    du.save_cluster_centers(K.cluster_centers_, "clusters.npy")
    print("Done")

    # Convert each sample into histogram of bag of features
    print("Converting to histograms...",)
    generate_histogram = lambda x: np.histogram(K.predict(x), 
            bins = range(cluster_size))
    transformed = list(map(generate_histogram, descriptors))
    print(transformed)
    print("Done")
    packed = list(zip(_class, transformed))
    du.write_data(args.outputfile, packed)



