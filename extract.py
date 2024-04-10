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
    neos_columns = ['pdes', 'name', 'pha', 'diameter']
    with open(f'{neo_csv_path}', 'r') as infile:
        reader = csv.DictReader(infile)
        df = []
        for row in reader:
            selection = {column: row[column] for column in neos_columns}
            df.append(selection)
    
    neolist = []
    for i in range(len(df)):
        lst = []
        for key, value in df[i].items():
            lst.append(value)
        neo = NearEarthObject(designation = lst[0], name = lst[1], hazardous = lst[2], diameter = lst[3])
        neolist.append(neo)

    return neolist


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es. (columns of interest)
    """
    with open(f'{cad_json_path}', 'r') as infile:
        data = json.load(infile)
    data['fields'] = ['des','cd','dist','v_rel']
    data['data'] = [[data['data'][i][0], data['data'][i][3],data['data'][i][4], data['data'][i][7]] for i in range(len(data['data']))] #Option: can be adjusted with the loop below
    
    calist = []
    for i in range(len(data['data'])):
        designation = data['data'][i][0]
        time = data['data'][i][1]
        distance = data['data'][i][2]
        velocity = data['data'][i][3]
        ca = CloseApproach(_designation = designation, time = time, distance = distance, velocity = velocity)
        calist.append(ca)
    
    return calist

