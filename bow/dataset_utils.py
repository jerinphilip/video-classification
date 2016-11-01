from bow._utils import scanl
from operator import add
from collections import namedtuple
import pandas as pd
from functools import partial
import numpy as np

def extract(line):
    splits = list(map(float, line.split()))
    split_indices = [10, 30, 96, 108, 96, 96]
    indices = [0] + list(scanl(add, 0, split_indices))
    ranges = zip(indices[:-1], indices[1:])
    first, *rest = list(map(lambda x: splits[x[0]:x[1]], ranges))
    descriptors = list(map(np.array, rest))
    final_tuple = first + descriptors
    sample = namedtuple('sample', 'frameNum mean_x mean_y var_x var_y \
            length scale x_pos y_pos t_pos \
            Trajectory HOG HOF MBHx MBHy')
    return sample._make(final_tuple)



def read_trackers(descriptor, filename):
    with open(filename, 'r') as trajectory_file:
        modified_extract = lambda x: extract(x)._asdict()[descriptor]
        data = list(map(modified_extract, trajectory_file))
        return data

def extract_with_frameNum(descriptor, x):
    result = extract(x)._asdict()
    frameNum = int(result['frameNum'])
    feature = result[descriptor]
    return (frameNum, feature)

def postprocess_to_samples(data):
    fNos, features = zip(*data)
    start, end = min(fNos), max(fNos)
    data_new = [[] for i in range(end-start+1)]
    for (fno, feature) in data:
        data_new[fno-start].append(feature)
    return data_new




def read_trackers_by_volume(descriptor, filename):
    with open(filename, 'r') as trajectory_file:
        #modified_extract = lambda x: extract(x)._asdict()[descriptor]
        modified_extract = partial(extract_with_frameNum, descriptor)
        data = list(map(modified_extract, trajectory_file))
        data = postprocess_to_samples(data)
        return data


def read_data(metafile, descriptor, frac):
    entries = pd.read_csv(metafile, delimiter=',', header=0)
    entries = entries.sample(frac=frac)
    rt_modified = partial(read_trackers, descriptor)
    tracker_data = list(map(rt_modified, entries["filename"]))
    data = list(zip(entries["class"], tracker_data))
    return data

def write_data(outputfile, mapping):
    data = pd.DataFrame(mapping, columns=['class', 'histogram'])
    data.to_csv(outputfile, delimiter=',')

def save_cluster_centers(cluster_centers, fname):
    cluster_centers = list(map(np.array, cluster_centers))
    np.save(fname, cluster_centers)

def read_kmeans(filename):
    parse = lambda line: list(map(float, line.strip().split(' ')))[1:]
    with open(filename, 'r') as meanfile:
        means = list(map(parse, meanfile))
        return np.array(means)
