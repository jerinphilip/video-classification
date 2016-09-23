from parser import create_parser
#from matplotlib import pyplot as plt
#import matplotlib.colors
from functools import partial, reduce
from dataset_utils import read_data, write_data
from operator import add
import cluster_utils as cu
import numpy as np



if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    np.random.seed(42)

    cluster_size = 6

    # Extract data.
    data = read_data(args.metafile, args.descriptor)
    _class, descriptors = zip(*data)

    descriptors_flattened = np.array(reduce(add, descriptors))
    # Generate K Means
    K = cu.generate_BagOfWords(descriptors_flattened, cluster_size)

    # Convert each sample into histogram of bag of features
    generate_histogram = lambda x: np.histogram(K.predict(x), 
            bins = range(cluster_size))
    tranformed = list(map(generate_histogram, descriptors))
    packed = list(zip(_class, tranformed))
    write_data(args.outputfile, packed)



