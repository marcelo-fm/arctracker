# Name: Trend_3d_Ex_02.py
# Description: Interpolate a series of point features onto a
#              rectangular raster using a trend technique.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outRaster = "C:/sapyexamples/output/trendout02"
cellSize = 2000.0
PolynomialOrder = 2
regressionType = "LINEAR"


# Execute Trend
arcpy.ddd.Trend(inPointFeatures, zField, outRaster, cellSize, 
               PolynomialOrder, regressionType)