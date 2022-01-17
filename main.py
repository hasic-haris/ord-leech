"""
Author:
    Haris Hasic, PhD Student
Institution:
    Ishida Laboratory, Department of Computer Science, School of Computing, Tokyo Institute of Technology
Updated on:
    January 12th, 2022
"""

import os

from argparse import Namespace

from helpers.argument_parser import parse_arguments
from helpers.ord_dataset_parser import get_ord_dataset_metadata, get_ord_dataset_contents


def main(args: Namespace = None) -> None:
    """ The main function of the project. """

    args.data_path = "/nasa/datasets/open_reaction_database/ord-data/"

    for directory in os.listdir(os.path.join(args.data_path, "data")):
        for pb_file in os.listdir(os.path.join(args.data_path, "data", directory)):
            dataset_file_path = os.path.join(args.data_path, "data", directory, pb_file)

            # print(get_ord_dataset_metadata(dataset_file_path=dataset_file_path))

            get_ord_dataset_contents(dataset_file_path=dataset_file_path)

            print("-----------------------------------------------------------")
            #break
        #break





if __name__ == "__main__":
    main(parse_arguments())
