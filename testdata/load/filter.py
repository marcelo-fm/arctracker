# Name: Filter_Ex_02.py
# Description: Performs a preset focal filter on a raster. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation" 

# Execute Filter
filterOut =  Filter(inRaster, "LOW", "") 

# Save the output 
filterOut.save("C:/sapyexamples/output/filterout")