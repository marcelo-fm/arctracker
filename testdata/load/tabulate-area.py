# Name: TabulateArea_Ex_02.py
# Description: Calculates cross tabulated areas between two datasets.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"
env.extent = "classgrid"
env.snapRaster = "classgrid"

# Set local variables
inZoneData = "zonedata.shp"
zoneField = "IDStr"
inClassData = "valueraster"
classField = "VALUE"
outTable = "C:/sapyexamples/output/areatable02.dbf"
processingCellSize = 2

# Execute TabulateArea
TabulateArea(inZoneData, zoneField, inClassData, classField, outTable,
             processingCellSize)