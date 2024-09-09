# Name: Int_Ex_02.py
# Description: Converts each cell value of a raster to an integer by truncation
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "gwhead"

# Execute Int
outInt = Int(inRaster)

# Save the output 
outInt.save("C:/sapyexamples/output/outint")