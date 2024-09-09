# Name: AlterDomain.py
# Description: Modify an attribute domain to constrain valid date
#              range for wildlife sightings.
# Author: ESRI
 
# Import system modules
import arcpy
from arcpy import env
 
# Set the workspace
env.workspace = "C:/data"
 
# Set local parameters
gdb = "Habitat.gdb"
domName = "CoastalArea"
new_domName = "SightingSeason"
new_desc = "Range of valid dates for sightings"
new_split = "DUPLICATE"
new_merge = "AREA_WEIGHTED"

# Process: Modify the range domain
arcpy.AlterDomain_management(gdb, domName, new_domName, new_desc, new_split, new_merge)