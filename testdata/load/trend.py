# Name: Trend_Ex_02.py
# Description: Interpolate a series of point features 
#    onto a rectangular raster using a trend technique.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
cellSize = 2000.0
PolynomialOrder = 2
regressionType = "LINEAR"


# Execute Trend
outTrend = Trend(inPointFeatures, zField, cellSize, 
                 PolynomialOrder, regressionType)

# Save the output 
outTrend.save("C:/sapyexamples/output/trendout02")