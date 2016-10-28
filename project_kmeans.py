import bow.dataset_utils as du
import bow.cluster_utils as cu
import pandas as pd
from parser import create_parser_kmeans
from functools import partial

def generate_histogram(kmeans, descriptors):
    r, c = kmeans.shape
    #print("Computing")
    #print("Shape ",r,c)
    vecs = [0 for i in range(r)]
    for i, vec in enumerate(descriptors):
        vecs[cu.find_nearest(kmeans,vec)] += 1;
    return vecs


def read_data(metafile, descriptor, frac, kmeans):
    entries = pd.read_csv(metafile, delimiter=',', header=0)
    entries = entries.sample(frac=frac)
    #rt_modified = partial(read_trackers, descriptor)
    #tracker_data = list(map(rt_modified, entries["filename"]))
    result = []
    for (label, fname) in zip(entries["class"], entries["filename"]):
            print(label, fname)
            data = du.read_trackers(descriptor, fname)
            hgram = generate_histogram(kmeans, data)
            result.append((label, hgram))
    return result

def convert(h):
    L = list(enumerate(h))
    cell_f = lambda x: ':'.join(list(map(str, x)))
    J = map(cell_f, L)
    return ' '.join(J)

def serialize(exported):
    #print(exported)
    labels, hgrams = zip(*exported)
    unique = list(set(labels))
    unique.sort()
    label_ids = list(map(lambda x: unique.index(x), labels))
    outstrings = []
    for (l, h) in zip(label_ids, hgrams):
        outstring = str(l) + ' ' + convert(h)
        outstrings.append(outstring)
    return '\n'.join(outstrings)






if __name__ == '__main__':
    parser = create_parser_kmeans()
    args = parser.parse_args()
    means = du.read_kmeans(args.kmeans)
    print("Reading data...")
    data = read_data(args.metafile, args.descriptor, 1, means)
    f_input = open("svm_input.txt",'w')
    outstring = serialize(data)
    f_input.write(outstring)
    f_input.close()
    print("Done.")
