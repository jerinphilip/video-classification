import numpy as np
def perprocessing(ip):
    classes = []
    vectors = []
    for i in len(ip):
        classes += ip[i][0]
        tmp = ip[i]
        tmp = tmp[1:len(tmp)]
        tmp = [tmp]
        vectors = np.concatenate((vectors,tmp))
