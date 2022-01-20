""" The definition of the Open Reaction Database chemical reaction entry processing utility functions. """

from typing import Optional, List

from google.protobuf.json_format import MessageToDict
from ord_schema.proto.reaction_pb2 import Reaction, ReactionIdentifier, CompoundIdentifier


# noinspection PyBroadException
def get_reaction_identifiers(reaction_message: Reaction) -> Optional[List]:
    """ Get the identifiers of a single Open Reaction Database chemical reaction entry. """

    reaction_id, reaction_name, reaction_smiles = None, None, None

    # Identifiers Data #1: Reaction ID
    try:
        reaction_id = reaction_message.reaction_id
    except:
        pass

    # Identifiers Data #2: Reaction Name and SMILES
    try:
        for reaction_identifier in reaction_message.identifiers:
            if reaction_identifier.type == ReactionIdentifier.NAME:
                reaction_name = reaction_identifier.value
            if reaction_identifier.type in [ReactionIdentifier.REACTION_SMILES, ReactionIdentifier.REACTION_CXSMILES]:
                reaction_smiles = reaction_identifier.value
    except:
        pass

    return [reaction_id, reaction_name, reaction_smiles]


# noinspection PyBroadException
def get_reaction_inputs(reaction_message: Reaction) -> Optional[List]:
    """ Get the inputs of a single Open Reaction Database chemical reaction entry. """

    input_labels, input_names, input_smiles, input_roles, input_amounts, input_amount_units = [], [], [], [], [], []

    for input_key, input_value in sorted(reaction_message.inputs.items()):
        for input_component in input_value.components:
            name, smiles, reaction_role, amounts, amount_units = None, None, None, [], []

            # Inputs Data #1: Input Compound Name and SMILES
            try:
                for input_identifier in input_component.identifiers:
                    if input_identifier.type == CompoundIdentifier.NAME:
                        name = input_identifier.value
                    if input_identifier.type in [CompoundIdentifier.SMILES, CompoundIdentifier.CXSMILES]:
                        smiles = input_identifier.value
            except:
                pass

            # Inputs Data #2: Input Compound Role
            try:
                reaction_role = MessageToDict(input_component)["reactionRole"]
            except:
                pass

            # Inputs Data #3: Input Compound Amounts and Amount Units
            try:
                for input_amount in MessageToDict(input_component.amount).values():
                    amounts.append(input_amount["value"])
                    amount_units.append(input_amount["units"])
            except:
                pass

            input_labels.append(input_key)
            input_names.append(name)
            input_smiles.append(smiles)
            input_roles.append(reaction_role)
            input_amounts.append(amounts)
            input_amount_units.append(amount_units)

    return [input_labels, input_names, input_smiles, input_roles, input_amounts, input_amount_units]


# noinspection PyBroadException
def get_reaction_conditions(reaction_message: Reaction) -> Optional[List]:
    """ Get the conditions of a single Open Reaction Database chemical reaction entry. """

    setpoint_temperature, setpoint_temperature_unit, control_temperature = None, None, None
    atmosphere_pressure, control_pressure = None, None

    # Conditions Data #1: Temperature
    try:
        for temperature_key, temperature_value in MessageToDict(reaction_message.conditions.temperature).items():
            if temperature_key == "setpoint":
                setpoint_temperature = temperature_value["value"]
                setpoint_temperature_unit = temperature_value["units"]
            if temperature_key == "control":
                control_temperature = temperature_value["type"]
    except:
        pass

    # Conditions Data #2: Pressure
    try:
        for pressure_key, pressure_value in MessageToDict(reaction_message.conditions.pressure).items():
            if pressure_key == "atmosphere":
                atmosphere_pressure = pressure_value["type"]
            if pressure_key == "control":
                control_pressure = pressure_value["type"]
    except:
        pass

    return [setpoint_temperature, setpoint_temperature_unit, control_temperature,
            atmosphere_pressure, control_pressure]


# noinspection PyBroadException
def get_reaction_outcomes(reaction_message: Reaction) -> Optional[List]:
    """ Get the outcomes of a single Open Reaction Database chemical reaction entry. """

    outcome_times, outcome_time_units, outcome_names, outcome_smiles, outcome_roles = [], [], [], [], []
    outcome_yields, outcome_amounts, outcome_amount_units = [], [], []

    for reaction_outcome in reaction_message.outcomes:
        reaction_time, reaction_time_unit = None, None

        # Outcomes Data #1: Reaction Time
        try:
            for outcome_key, outcome_value in MessageToDict(reaction_outcome).items():
                if outcome_key == "reactionTime":
                    reaction_time = outcome_value["value"]
                    reaction_time_unit = outcome_value["units"]
        except:
            pass

        for reaction_product in reaction_outcome.products:
            name, smiles, reaction_role, yields, amounts, amount_units = None, None, None, [], [], []

            # Outcomes Data #2: Outcome Compound Name and SMILES
            try:
                for outcome_identifier in reaction_product.identifiers:
                    if outcome_identifier.type == CompoundIdentifier.NAME:
                        name = outcome_identifier.value
                    if outcome_identifier.type in [CompoundIdentifier.SMILES, CompoundIdentifier.CXSMILES]:
                        smiles = outcome_identifier.value
            except:
                pass

            # Outcomes Data #3: Outcome Compound Role
            try:
                reaction_role = MessageToDict(reaction_product)["reactionRole"]
            except:
                pass

            # Outcomes Data #4: Outcome Compound Amounts and Amount Units
            try:
                for outcome_measurement in reaction_product.measurements:
                    outcome_measurement_dict = MessageToDict(outcome_measurement)

                    if outcome_measurement_dict["type"] == "YIELD":
                        yields.append(outcome_measurement_dict["percentage"]["value"])
                    if outcome_measurement_dict["type"] == "AMOUNT":
                        for outcome_amount in outcome_measurement_dict["amount"].values():
                            amounts.append(outcome_amount["value"])
                            amount_units.append(outcome_amount["units"])
            except:
                pass

            outcome_names.append(name)
            outcome_smiles.append(smiles)
            outcome_roles.append(reaction_role)
            outcome_yields.append(yields)
            outcome_amounts.append(amounts)
            outcome_amount_units.append(amount_units)

        outcome_times.append(reaction_time)
        outcome_time_units.append(reaction_time_unit)

    return [outcome_times, outcome_time_units, outcome_names, outcome_smiles, outcome_roles,
            outcome_yields, outcome_amounts, outcome_amount_units]


def process_reaction_entry(reaction_message: Reaction, verbose: bool = False) -> Optional[List]:
    """ Process an individual chemical reaction entry by extracting the reaction identifier, inputs, conditions and
    outcomes information. """

    try:
        reaction_data = get_reaction_identifiers(reaction_message=reaction_message)
        reaction_data.extend(get_reaction_inputs(reaction_message=reaction_message))
        reaction_data.extend(get_reaction_conditions(reaction_message=reaction_message))
        reaction_data.extend(get_reaction_outcomes(reaction_message=reaction_message))

        return reaction_data

    except Exception as exception_handle:
        if verbose:
            print("Exception occurred during the handling of the Open Reaction Database chemical reaction entries. "
                  f"Detailed message:\n{exception_handle}")

        return None

