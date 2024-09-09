# Name: NaturalNeighbor_3d_Ex_02.py
# Description: Interpolate a series of point features onto 
#    a rectangular raster using Natural Neighbor interpolation.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inPntFeat = "ca_ozone_pts.shp"
zField = "ozone"
outRaster = "C:/output/nnout"
cellSize = 40000

# Execute NaturalNeighbor
arcpy.ddd.NaturalNeighbor(inPntFeat, zField, outRaster, cellSize)