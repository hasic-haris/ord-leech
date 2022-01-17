""" The definition of the database file parser helper functions. """

import re

from tqdm import tqdm
from typing import Dict, Tuple

import pandas as pd


from ord_schema.proto.dataset_pb2 import Dataset
from ord_schema.proto.reaction_pb2 import Reaction, ReactionRole, ReactionIdentifier

from ord_schema import message_helpers
from ord_schema.message_helpers import load_message
from ord_schema.validations import validate_message

from google.protobuf.json_format import MessageToDict
import gzip


def get_reaction_inputs(reaction: Reaction):
    """ Description text goes here. """

    for reaction_input in reaction.inputs.items():
        print(reaction_input)
        print()




"""


def get_reaction_inputs(reaction: Reaction, allow_incomplete=False):

    reactants, agents = set(), set()
    roles = ReactionRole

    for key, value in sorted(reaction.inputs.items()):
        for compound in reaction.inputs[key].components:
            try:
                smiles = message_helpers.smiles_from_compound(compound)
            except ValueError as error:
                if allow_incomplete:
                    continue
                raise error
            if compound.reaction_role in [
                roles.REAGENT, roles.SOLVENT, roles.CATALYST
            ]:
                agents.add(smiles)
            elif compound.reaction_role == roles.INTERNAL_STANDARD:
                continue
            else:
                reactants.add(smiles)

    print(reactants)
    print(agents)


def get_reaction_conditions(reaction: Reaction):

    recorded_yields = []

    #for reaction_conditions in reaction.conditions:
    print(reaction.conditions)


def get_reaction_outcomes(reaction: Reaction):

    recorded_products, product_desirability, recorded_yields = [], [], []

    print(message_helpers.get_reaction_smiles(reaction, generate_if_missing=True))
    
    for reaction_outcome in reaction.outcomes:
        for product_ind, product in enumerate(reaction_outcome.products):
            product_desirability.append(product.is_desired_product)
            recorded_yields.append([])

            for identifier in product.identifiers:
                if identifier.type == identifier.SMILES:
                    recorded_products.append(identifier.value)

            for measurement in product.measurements:
                if measurement.type == measurement.YIELD:
                    recorded_yields[product_ind].append(round(measurement.percentage.value, 2))

    print(tuple(recorded_products))
    print(tuple(recorded_yields))
    print(tuple(product_desirability))
    print()

    return recorded_yields

"""