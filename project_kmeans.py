import bow.dataset_utils as du
import bow.cluster_utils as cu
from parser import create_parser_kmeans
from functools import partial

def generate_histogram(kmeans, descriptors):
    r, c = kmeans.shape
    print("Computing")
    #print("Shape ",r,c)
    vecs = [0 for i in range(r)]
    for i, vec in enumerate(descriptors):
        vecs[cu.find_nearest(kmeans,vec)] += 1;
    return vecs


if __name__ == '__main__':
    parser = create_parser_kmeans()
    args = parser.parse_args()
    print("Reading data...",)
    data = du.read_data(args.metafile, args.descriptor, 1)
    print("Done.")
    _class, descriptors = zip(*data)
    means = du.read_kmeans(args.kmeans)
    f = partial(generate_histogram, means)
    rep = list(map(f, descriptors))
    print(rep)
