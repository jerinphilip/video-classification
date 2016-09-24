
import argparse

def create_parser():
    arguments = [
        ['-i', '--input', "input filename", str, "metafile"],
        ['-d', '--descriptor', "Descriptor to use", str, "descriptor"],
        ['-o', '--output', "Output filenam", str, "outputfile"],
        #['-v', '--validate', "validation set", str, 'validation_set']
    ]

    parser = argparse.ArgumentParser(description="Helper Script")
    for arg in arguments:
        unix, gnu, desc, typename, dest = arg
        parser.add_argument(unix, gnu, help=desc, type=typename, 
                required=True, dest=dest)
    return parser
