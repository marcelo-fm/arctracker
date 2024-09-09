# Name: Times_Ex_02.py
# Description: Multiplies the values of two rasters on a cell-by-cell basis.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
inConstant = 0.3048

# Execute Times
outTimes = Times(inRaster, inConstant)

# Save the output 
outTimes.save("C:/sapyexamples/output/timesout")