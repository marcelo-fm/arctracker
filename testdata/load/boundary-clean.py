# Name: BoundaryClean_Ex_02.py
# Description: Smoothes the boundary between zones 
#              by expanding and shrinking it.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "land"

# Execute BoundaryClean
OutBndCln = BoundaryClean(inRaster, "ASCEND", "TWO_WAY")

# Save the output 
OutBndCln.save("c:/sapyexamples/output/bndcln_asc2")