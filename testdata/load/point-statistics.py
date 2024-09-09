# Name: PointStatistics_Ex_02.py
# Description: Calculates a statistic on points over a specified 
#    neighborhood outputting a raster.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
field = "OZONE"
cellSize = 500
neighborhood = NbrCircle(6000, "MAP")

# Execute PointStatistics
outPointStatistics = PointStatistics(inPointFeatures, field, cellSize,
                                     neighborhood, "MEAN")

# Save the output 
outPointStatistics.save("C:/sapyexamples/output/pointstatout")