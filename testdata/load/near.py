# Name: features_closest_to_input.py

"""
    This script finds, for each input feature, a list of near feature it is closest to.
    If near features 6, 7, 10 are closest to input feature 3 then the 
    resulting dictionary will have a list [6, 7, 10] as value for key 3
"""

import os
import arcpy

in_fc = r"C:\data\cities.gdb\cities_many"

# create a dictionary to hold the list of near ids for each input id
nearest_dict = dict()

with arcpy.da.SearchCursor(in_fc, ["OID@", "NEAR_FID"]) as rows:
    for row in rows:
        nearest_id = row[0]  # get OID value for that row
        input_id = row[1]    # get NEAR_FID value 
        
        if input_id in nearest_dict:
            # if a dict key already exists, append near id to value list for that key
            nearest_dict[input_id].append(nearest_id)
        else:
            # if the key does not exist then create a new list with near id
            # and add it to the dictionary
            nearest_dict[input_id] = [nearest_id]
            
print(nearest_dict)

# output will look like:
# {1: [13, 28], 2: [2, 9, 14, 20, 22], 3: [11, 12, 24, 25]}