# Name: Cutfill_Ex_02.py
# Description: Calculates the volume and area of cut and 
#              fill locations.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inBeforeRaster = "elevation01"
inAfterRaster =  "elevation02"
zFactor = 0.5

# Execute CutFill
outCutFill = CutFill(inBeforeRaster, inAfterRaster, zFactor)

# Save the output 
outCutFill.save("C:/sapyexamples/output/outcutfill02")