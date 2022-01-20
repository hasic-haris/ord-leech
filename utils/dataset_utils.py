""" The definition of the Open Reaction Database dataset processing utility functions. """

import os

import multiprocessing as mp
import pandas as pd

from datetime import datetime
from tqdm import tqdm

from ord_schema import message_helpers
from ord_schema.proto.dataset_pb2 import Dataset

from utils.reaction_utils import process_reaction_entry


def get_dataset_metadata(data_directory_path: str, output_directory_path: str = None) -> None:
    """ Get the metadata of all available datasets from the Open Reaction Database. """

    try:
        ids, names, descriptions, row_counts = [], [], [], []

        for directory_name in tqdm(
                iterable=os.listdir(data_directory_path),
                total=len(os.listdir(data_directory_path)),
                ascii=True,
                ncols=150,
                desc=f"Reading the Open Reaction Database dataset files"
        ):
            for file_name in os.listdir(os.path.join(data_directory_path, directory_name)):
                file_contents = message_helpers.load_message(
                    filename=os.path.join(data_directory_path, directory_name, file_name),
                    message_type=Dataset
                )

                ids.append(file_contents.dataset_id)
                names.append(file_contents.name)
                descriptions.append(file_contents.description)
                row_counts.append(len(file_contents.reactions))

        metadata_dataframe = pd.DataFrame(data={
            "dataset_id": ids,
            "dataset_name": names,
            "dataset_description": descriptions,
            "dataset_row_count": row_counts}
        )

        if output_directory_path is not None:
            metadata_dataframe.to_csv(
                os.path.join(output_directory_path, "{:%Y%m%d%H%M}_ord_metadata.csv".format(datetime.now())),
                index=False
            )

        print(f"\nThe metadata dataframe ({len(metadata_dataframe.index)}x{len(metadata_dataframe.columns)}) has been "
              "successfully generated!\n")

        print(metadata_dataframe.head(10))

    except Exception as exception_handle:
        raise Exception("Exception occurred during the handling of the Open Reaction Database dataset file metadata. "
                        f"Detailed message:\n{exception_handle}")


def get_dataset_contents(data_directory_path: str, merge_datasets: bool = False, output_directory_path: str = None,
                         num_cores: int = 1) -> None:
    """ Get the contents of the specified datasets from the Open Reaction Database. """

    try:
        merged_contents_dataframes = []

        for directory_ind, directory_name in enumerate(os.listdir(data_directory_path)):
            for file_name in os.listdir(os.path.join(data_directory_path, directory_name)):
                file_contents = message_helpers.load_message(
                    filename=os.path.join(data_directory_path, directory_name, file_name),
                    message_type=Dataset
                )

                with mp.Pool(num_cores if 0 < num_cores <= mp.cpu_count() else 1) as process_pool:
                    processing_results = [
                        processed_entry for processed_entry in tqdm(
                            iterable=process_pool.imap(process_reaction_entry, file_contents.reactions),
                            total=len(file_contents.reactions),
                            ascii=True,
                            ncols=150,
                            desc=f"Processing the '{file_contents.dataset_id}' "
                                 f"({directory_ind+1}/{len(os.listdir(data_directory_path))}) "
                                 f"dataset (Cores: {num_cores})")
                    ]

                    process_pool.close()
                    process_pool.join()

                    contents_dataframe = pd.DataFrame(
                        data=processing_results,
                        columns=["reaction_id", "reaction_name", "reaction_smiles",

                                 "input_compound_labels", "input_compound_names", "input_compound_smiles",
                                 "input_roles", "input_compound_amounts", "input_compound_amount_units",

                                 "setpoint_temperature", "setpoint_temperature_unit", "control_temperature",
                                 "atmosphere_pressure", "control_pressure",

                                 "reaction_time", "reaction_time_units",

                                 "outcome_compound_names", "outcome_compound_smiles", "outcome_compound_roles",
                                 "outcome_compound_yields", "outcome_compound_amounts", "outcome_compound_amount_units"]
                    )

                    if merge_datasets:
                        merged_contents_dataframes.append(contents_dataframe)
                    else:
                        if output_directory_path is not None:
                            contents_dataframe.to_pickle(
                                os.path.join(
                                    output_directory_path,
                                    "{:%Y%m%d%H%M}_{}.pkl".format(datetime.now(), file_contents.dataset_id)
                                )
                            )

                        print(f"The contents dataframe for the '{file_contents.dataset_id}' dataset "
                              f"({len(contents_dataframe.index)}x{len(contents_dataframe.columns)}) has been "
                              "successfully generated!\n")

        if merge_datasets:
            dataset_dataframe = pd.concat(merged_contents_dataframes, ignore_index=True)

            if output_directory_path is not None:
                dataset_dataframe.to_pickle(
                    os.path.join(
                        output_directory_path,
                        "{:%Y%m%d%H%M}_all_datasets.pkl".format(datetime.now())
                    )
                )

            print(f"\nThe merged contents dataframe ({len(dataset_dataframe.index)}x{len(dataset_dataframe.columns)}) "
                  "has been successfully generated!\n")

    except Exception as exception_handle:
        raise Exception("Exception occurred during the handling of the Open Reaction Database dataset file contents. "
                        f"Detailed message:\n{exception_handle}")
