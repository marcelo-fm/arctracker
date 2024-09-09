# Name: FocalFlow_Ex_02.py
# Description: Determines the flow of the values in the 
#    input raster within each cell's immediate neighborhood.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
threshold = 5 

# Execute FocalFlow
outFocalFlow = FocalFlow(inRaster, threshold)

# Save the output 
outFocalFlow.save("C:/sapyexamples/output/focalflow")