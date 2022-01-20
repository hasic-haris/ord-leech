"""
Author:
    Haris Hasic
Affiliations:
    PhD Student @ Ishida Laboratory, Department of Computer Science, School of Computing, Tokyo Institute of Technology
    Research Engineer @ Elix Inc.
Updated on:
    January 21st, 2022
"""

from argparse import Namespace

from utils.argument_utils import parse_arguments
from utils.dataset_utils import get_dataset_metadata, get_dataset_contents


def main(args: Namespace = None) -> None:
    """ The main function of the project. """

    args.input_directory_path = "/data/hhasic/open_reaction_database/ord-data/data/"
    args.output_directory_path = "/data/hhasic/open_reaction_database/"
    args.extract_dataset_metadata = False
    args.merge_datasets = True
    args.num_cores = 10

    if args.extract_dataset_metadata:
        get_dataset_metadata(
            data_directory_path=args.input_directory_path,
            output_directory_path=args.output_directory_path
        )

    else:
        get_dataset_contents(
            data_directory_path=args.input_directory_path,
            merge_datasets=args.merge_datasets,
            output_directory_path=args.output_directory_path,
            num_cores=args.num_cores
        )


if __name__ == "__main__":
    main(parse_arguments())
