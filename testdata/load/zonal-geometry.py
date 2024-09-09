# Name: ZonalGeometry_Ex_02.py
# Description:Calculates for each zone in a dataset the specified geometry 
#   measure (area, perimeter, thickness, or the characteristics 
#   of ellipse).
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inZoneData = "zones.shp"
zoneField = "Classes"
cellSize = 0.2

# Execute ZonalStatistics
outZonalGeometry = ZonalGeometry(inZoneData, zoneField, "AREA", cellSize)  

# Save the output 
outZonalGeometry.save("C:/sapyexamples/output/zonegeomout2")