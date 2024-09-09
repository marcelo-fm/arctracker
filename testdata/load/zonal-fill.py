# Name: ZonalFill_Ex_02.py
# Description: Fills zones using the minimum cell value from a weight 
#   raster, along the zone boundary.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inZoneRaster = "inzone"
zoneWeightRaster = "zoneweight"

# Execute ZonalStatistics
outZonalFill = ZonalFill(inZoneRaster, zoneWeightRaster)

# Save the output 
outZonalFill.save("C:/sapyexamples/output/zonefillout3")