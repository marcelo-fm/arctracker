# Name: Cutfill_3d_Ex_02.py
# Description: Calculates the volume and area of cut and 
#              fill locations.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inBeforeRaster = "elevation01"
inAfterRaster =  "elevation02"
outRaster = "C:/output/outcutfill02"
zFactor = 0.5

# Execute CutFill
arcpy.ddd.CutFill(inBeforeRaster, inAfterRaster, outRaster, zFactor)