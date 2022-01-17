""" The definition of the argument parser helper functions. """

from argparse import ArgumentParser, Namespace


def parse_arguments(parser_description: str = None) -> Namespace:
    """ Parse the specified command line arguments. """

    argument_parser = ArgumentParser(description=parser_description)

    argument_parser.add_argument(
        "-d",
        "--data-path",
        type=str,
        required=False,
        help="The 'ord-data' folder path.",
    )

    return argument_parser.parse_args()
