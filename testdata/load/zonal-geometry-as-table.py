# Name: ZonalGeometryAsTable_Ex_02.py
# Description:Calculates for each zone in a dataset the specified geometry 
#   measure (area, perimeter,  thickness, or the characteristics 
#   of ellipse) and reports the results as a table.
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
outTable = "zonalgeomout02.dbf"
processingCellSize = 0.2

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute ZonalGeometryAsTable
outZonalGeometryAsTable = ZonalGeometryAsTable(inZoneData, zoneField, outTable, processingCellSize)