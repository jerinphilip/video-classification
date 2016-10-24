import bow.dataset_utils as du
import bow.cluster_utils as cu
from parser import create_parser_kmeans

if __name__ == '__main__':
    parser = create_parser_kmeans()
    args = parser.parse_args()
    print("Reading data...",)
    data = du.read_data(args.metafile, args.descriptor, 1)
    print(data)
    print("Done.")
    _class, descriptors = zip(*data)
    means = du.read_kmeans(args.kmeans)
