# Name: Aggregate_Ex_02.py
# Description: Generates a reduced resolution version of a raster.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "highres"
cellFactor = 3

# Execute Aggregate
outAggreg = Aggregate(inRaster, cellFactor, "MEAN", "TRUNCATE", "NODATA")

# Save the output 
outAggreg.save("C:/sapyexamples/output/aggregate02")