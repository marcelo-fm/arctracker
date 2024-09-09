# Name: ExtractMultiValuesToPoints_Ex_02.py
# Description: Extracts the cells of multiple rasters as attributes in
#    an output point feature class.  This example takes a multiband IMG
#    and two GRID files as input.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPointFeatures = "poi.shp"
inRasterList = [["doqq.img", "doqqval"], ["redstd", "focalstd"], 
                ["redmin", "focalmin"]]

# Execute ExtractValuesToPoints
ExtractMultiValuesToPoints(inPointFeatures, inRasterList, "BILINEAR")