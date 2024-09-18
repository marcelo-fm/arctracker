# Name: EqualToFrequency_Ex_02.py
# Description: Evaluates the number of times a set of rasters is
#              equal to another raster on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inValueRaster = "cost"
inRaster01 = "degs"
inRaster02 = "negs"
inRaster03 = "fourgrd"

# Execute EqualToFrequency
outETF = EqualToFrequency(inValueRaster, [inRaster01, inRaster02, inRaster03])

# Save the output 
outETF.save("C:/sapyexamples/output/outETF")