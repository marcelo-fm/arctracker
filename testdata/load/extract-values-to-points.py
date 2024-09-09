# Name: ExtractValuesToPoints_Ex_02.py
# Description: Extracts the cells of a raster based on a set of points.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPointFeatures = "rec_sites.shp"
inRaster = "elevation"
outPointFeatures = "C:/sapyexamples/output/extractvaluespts.shp"

# Execute ExtractValuesToPoints
ExtractValuesToPoints(inPointFeatures, inRaster, outPointFeatures,
                      "INTERPOLATE", "VALUE_ONLY")