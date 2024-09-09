# Name: ASin_Ex_02.py
# Description: Calculates the inverse sine of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute ASin
outASin = ASin(inRaster)

# Save the output 
outASin.save("C:/sapyexamples/output/outasin.img")