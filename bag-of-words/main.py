from parser import create_parser
#from matplotlib import pyplot as plt
#import matplotlib.colors
from functools import partial, reduce
from dataset_utils import read_data
from operator import add
import cluster_utils as cu
import numpy as np



if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    # Extract data.
    data = read_data(args.descriptors, "HOG")
    _class, descriptors = zip(*data)

    descriptors_flattened = np.array(reduce(add, descriptors))
    words = cu.generate_BagOfWords(descriptors_flattened, 3)
    change_basis = lambda x: cu.generate_histograms(words, x)
    transform = lambda x: list(map(change_basis, x))
    transformed = list(map(transform, descriptors))
    for i in range(len(_class)):
        print(_class[i], len(transformed[i]))
    
    



