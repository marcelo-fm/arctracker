# Name: ReclassByTable_Ex_02.py
# Description: Reclassifies the values of the input raster using a remap table.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "slope"
inRemapTable = "remapslope"
outRaster = "C:/output/recslope"

# Execute Reclassify
arcpy.ddd.ReclassByTable(inRaster, inRemapTable, outRaster, "FROM","TO","OUT",
                        "NODATA")