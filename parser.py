
import argparse

def base_create_parser(arguments):
    parser = argparse.ArgumentParser(description="Helper Script")
    for arg in arguments:
        unix, gnu, desc, typename, dest = arg
        parser.add_argument(unix, gnu, help=desc, type=typename, 
                required=True, dest=dest)
    return parser

def create_parser():
    arguments = [
        ['-i', '--input', "input filename", str, "metafile"],
        ['-d', '--descriptor', "Descriptor to use", str, "descriptor"],
        ['-o', '--output', "Output filename", str, "outputfile"],
        #['-v', '--validate', "validation set", str, 'validation_set']
    ]
    return base_create_parser(arguments)


def create_parser_cuda():
    arguments = [ 
        ['-i', '--input', "input filename", str, "metafile"],
        ['-d', '--descriptor', "Descriptor to use", str, "descriptor"],
        ['-o', '--output', "Output filename", str, "outputfile"],
        ['-c', '--cudaoutfile', "Data output for Cuda", str, "cudaout"],
        #['-v', '--validate', "validation set", str, 'validation_set']
    ]   

    return base_create_parser(arguments)
    parser = argparse.ArgumentParser(description="Helper Script")

def create_parser_kmeans():
    arguments = [
        ['-i', '--input', "input filename", str, "metafile"],
        ['-d', '--descriptor', "Descriptor to use", str, "descriptor"],
        ['-k', '--kmeans', "Output filename", str, "kmeans"],
        #['-v', '--validate', "validation set", str, 'validation_set']
    ]
    return base_create_parser(arguments)
