# Name: GenerateNearTable.py
# Description: Finds 3 nearest in the near feature class from the input feature class.


# import system modules
import arcpy

# set workspace environment
arcpy.env.workspace = "C:/data/input/gnt.gdb"

# set required parameters 
in_features = "campsites"
near_features = ["parks", "trails"]
out_table = "near_parks_trails"

# optional parameters
search_radius = '1500 Meters'
location = 'NO_LOCATION'
angle = 'NO_ANGLE'
closest = 'ALL'
closest_count = 3

# find crime locations within the search radius
arcpy.analysis.GenerateNearTable(in_features, near_features, out_table, search_radius, 
                                 location, angle, closest, closest_count)