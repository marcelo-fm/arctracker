# Name: ExtractValuesToTable_Example_02.py
# Description: Extract the cell values from a raster, based on 
#              a point feature class, to a table.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/gapyexamples/data"

# Set local variables
inPoints = "C:/gapyexamples/data/ca_ozone_pts.shp"
raster = "C:/gapyexamples/data/inraster"
outTable = "C:/gapyexamples/output/outEVFR.dbf"

# Execute ExtractValuesToTable
arcpy.ExtractValuesToTable_ga(inPoints, raster, outTable, "", "")