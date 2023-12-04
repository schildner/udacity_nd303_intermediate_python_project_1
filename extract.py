"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = {}
    # TODO-> DONE: Load NEO data from the given CSV file.
    with open(neo_csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # primary designation, hazardous, name (sometimes missing), diameter (sometimes missing)
            pdes = row['pdes']
            pha = True if row['pha'] == 'Y' else False
            name = row['name'] if row['name'] != '' else None
            diameter = row['diameter'] if row['diameter'] != '' else 'nan'

            neo = NearEarthObject(pdes, pha, name, diameter)
            neos[pdes] = neo

    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    close_approaches = []

    # TODO-> DONE: Load close approach data from the given JSON file.
    with open(cad_json_path) as f:
        cad_map = json.load(f)
        approaches_rawdata = cad_map['data']

    for row in approaches_rawdata:
        # Interested only in subset of items in cad list:
        primary_designation = row[0]  # des item
        approach_datetime = row[3]    # cd item
        approach_distance = row[4]    # dist item
        relative_velocity = row[7]    # v_rel item
        ca = CloseApproach(primary_designation, approach_datetime, float(approach_distance), float(relative_velocity))
        close_approaches.append(ca)

    return close_approaches
