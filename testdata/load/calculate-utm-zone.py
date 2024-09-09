# Name: calculateutmzone_example.py
# Description: Calculates a custom UTM zone for a set of features
# Author: ESRI

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
arcpy.env.workspace = "C:\Data\ProjectData.gdb"

# Set local variables
inFeatures = "US_states"
utmField = "UTM_zone"

# Execute CalculateUTMZone
arcpy.CalculateUTMZone_cartography(inFeatures, utmField)