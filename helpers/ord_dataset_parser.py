""" The definition of the Open Reaction Database dataset parser helper functions. """

from typing import Dict

from ord_schema import message_helpers
from ord_schema.proto.dataset_pb2 import Dataset

from helpers.db_file_parser import get_something


def get_ord_dataset_metadata(dataset_file_path: str) -> Dict:
    """ Get the metadata of a single Open Reaction Database dataset file. """

    try:
        dataset_file_contents = message_helpers.load_message(filename=dataset_file_path, message_type=Dataset)

        return {
            "dataset_id": dataset_file_contents.dataset_id,
            "dataset_name": dataset_file_contents.name,
            "dataset_description": dataset_file_contents.description
        }

    except Exception as exception_handle:
        raise Exception("Exception occurred during the handling of the Open Reaction Database protocol buffer dataset "
                        f"file. Detailed message:\n{exception_handle}")


def get_ord_dataset_contents(dataset_file_path: str):
    """ Get the contents of a single Open Reaction Database dataset file. """

    try:
        dataset_file_contents = message_helpers.load_message(filename=dataset_file_path, message_type=Dataset)

        for reaction in dataset_file_contents.reactions:
            get_something(reaction=reaction)
            break

    except Exception as exception_handle:
        raise Exception("Exception occurred during the handling of the Open Reaction Database protocol buffer dataset "
                        f"file. Detailed message:\n{exception_handle}")

