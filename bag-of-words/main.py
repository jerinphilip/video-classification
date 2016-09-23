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

    # Extract data.
    data = read_data(args.metafile, args.descriptor)
    _class, descriptors = zip(*data)

    descriptors_flattened = np.array(reduce(add, descriptors))
    words = cu.generate_BagOfWords(descriptors_flattened, 6)
    change_basis = lambda x: cu.generate_histograms(words, x)
    transform = lambda x: list(map(change_basis, x))
    transformed = list(map(transform, descriptors))
    packed = list(zip(_class, transformed))
    write_data(args.outputfile, packed)



