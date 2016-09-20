from _utils import scanl
from operator import add
from collections import namedtuple
import pandas as pd
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


def read_trackers(filename):
    with open(filename, 'r') as trajectory_file:
        data = map(extract, trajectory_file)
        return data


def read_data(metafile):
    entries = pd.read_csv(metafile, delimiter=',', header=0)
    tracker_data = map(read_trackers, entries["filename"]
    data = zip(entries["class"], tracker_data)
    return data

if __name__ == '__main__':
    metafile = '../misc/ucf_sports.csv'
    print(read_data(metafile))
