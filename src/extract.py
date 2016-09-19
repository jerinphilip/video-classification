from _utils import scanl
from operator import add
from collections import namedtuple
import numpy as np

def extract(line):
    splits = list(map(float, line.split()))
    # frameNum mean_x mean_y var_x var_y length scale x_pos y_pos t_pos Trajectory HOG HOF MBHx MBHy
    #Trajectory:    2x[trajectory length] (default 30 dimension) 
    #HOG:           8x[spatial cells]x[spatial cells]x[temporal cells] (default 96 dimension)
    #HOF:           9x[spatial cells]x[spatial cells]x[temporal cells] (default 108 dimension)
    #MBHx:          8x[spatial cells]x[spatial cells]x[temporal cells] (default 96 dimension)
    #MBHy:          8x[spatial cells]x[spatial cells]x[temporal cells] (default 96 dimension)
    split_indices = [10, 30, 96, 108, 96, 96]
    indices = [0] + list(scanl(add, 0, split_indices))
    ranges = zip(indices[:-1], indices[1:])
    first, *rest = list(map(lambda x: splits[x[0]:x[1]], ranges))
    descriptors = list(map(np.array, rest))
    final_tuple = first + descriptors
    sample = namedtuple('sample', 'frameNum mean_x mean_y var_x var_y length scale x_pos y_pos t_pos \
            Trajectory HOG HOF MBHx MBHy')
    return sample._make(final_tuple)




def read_trackers(filename):
    with open(filename, 'r') as trajectory_file:
        data = map(extract, trajectory_file)
        return data


if __name__ == '__main__':
    print(read_trackers('out'))
