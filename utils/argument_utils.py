""" The definition of the argument parser utility functions. """

from argparse import ArgumentParser, Namespace


def parse_arguments(argument_parser_description: str = None) -> Namespace:
    """ Parse the specified command line arguments. """

    argument_parser = ArgumentParser(description=argument_parser_description)

    argument_parser.add_argument(
        "-in",
        "--input-directory-path",
        type=str,
        required=False,
        help="The full path to the '../ord-data/data' directory.",
    )

    argument_parser.add_argument(
        "-out",
        "--output-directory-path",
        type=str,
        default=None,
        help="The full path to a directory where the processing results can be stored. Default value is 'None'. "
             "If this path is not explicitly specified, the results are not stored at all.",
    )

    argument_parser.add_argument(
        "-metadata",
        "--extract-dataset-metadata",
        action="store_true",
        help="The flag to indicate the extraction of the metadata instead of the contents of all available datasets "
             "from the Open Reaction Database."
    )

    argument_parser.add_argument(
        "-merge",
        "--merge-datasets",
        action="store_true",
        help="The flag to indicate the merging of the contents of all available datasets from the "
             "Open Reaction Database."
    )

    argument_parser.add_argument(
        "-nc",
        "--num-cores",
        type=int,
        default=1,
        help="Number of CPU cores used for database processing. Default value is '1'.",
    )

    return argument_parser.parse_args()
