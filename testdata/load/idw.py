# Name: IDW_Ex_02.py
# Description: Interpolate a series of point features onto a rectangular 
#   raster using Inverse Distance Weighting (IDW).
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
power = 2
searchRadius = RadiusVariable(10, 150000)

# Execute IDW
outIDW = Idw(inPointFeatures, zField, cellSize, power, searchRadius)

# Save the output 
outIDW.save("C:/sapyexamples/output/idwout02")