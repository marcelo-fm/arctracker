# Name: ZonalHistogram_Ex_02.py
# Description: Creates a zonal histogram output table
#              showing the amount of value cells 
#              for each unique input zone.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inZoneData = "zonras"
zoneField = "zonfield"
inValueRaster = "valueras" 
outTable = "C:/sapyexamples/output/zonehist_tb2.dbf" 

# Execute ZonalHistogram
ZonalHistogram(inZoneData, zoneField, inValueRaster, outTable)