# Name: Kriging_3d_Ex_02.py
# Description: Interpolates a surface from points using kriging.
# Requirements: 3D Analyst Extension
# Import system modules

import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inFeatures = "ca_ozone_pts.shp"
field = "OZONE"
outRaster = "C:/output/krigoutput02"
cellSize = 2000
outVarRaster = "C:/output/outvariance"
kModel = "CIRCULAR"
kRadius = 20000

# Execute Kriging
arcpy.ddd.Kriging(inFeatures, field, outRaster, kModel, 
                 cellSize, kRadius, outVarRaster)