filename = 'kmeans_cuda/ucf_sports_actions_cuda.txt.cluster_centres'

def read_kmeans(filename):
    parse = lambda line: list(map(float, line.strip().split(' ')))
    with open(filename, 'r') as meanfile:
        means = list(map(parse, meanfile))
        return means



