# Name: NaturalNeighbor_Ex_02.py
# Description: Interpolate a series of point features onto a 
#    rectangular raster using Natural Neighbor interpolation.
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
cellSize = 40000

# Execute NaturalNeighbor
outNatNbr = NaturalNeighbor(inPointFeatures, zField, cellSize)

# Save the output 
outNatNbr.save("C:/sapyexamples/output/nnout02")