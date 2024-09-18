# Name: PrincipalComponents_Ex_02.py
# Description: Performs principal components analysis on a set of raster bands.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRasterBand1 = "redlands/redlandsc1"
inRasterBand2 = "redlands/redlandsc3"
numberComponents = 2
outDataFile = "C:/sapyexamples/output/pcdatafile.txt"

# Execute PrincipalComponents
outPrincipalComp = PrincipalComponents([inRasterBand1, inRasterBand2], 2,
                                       outDataFile)

# Save the output 
outPrincipalComp.save("C:/sapyexamples/output/outpc01")