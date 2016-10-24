import bow.dataset_utils as du
import bow.cluster_utils as cu
import pandas as pd
from parser import create_parser_kmeans

def read_data(metafile, descriptor, frac):
    entries = pd.read_csv(metafile, delimiter=',', header=0)
    entries = entries.sample(frac=frac)
    #rt_modified = partial(read_trackers, descriptor)
    #tracker_data = list(map(rt_modified, entries["filename"]))
    for x in entries:
        print(x)


if __name__ == '__main__':
    parser = create_parser_kmeans()
    args = parser.parse_args()
    _class, descriptors = zip(*data)
    means = du.read_kmeans(args.kmeans)
    print("Reading data...",)
    data = read_data(args.metafile, args.descriptor, 1)
    print(data)
    print("Done.")
