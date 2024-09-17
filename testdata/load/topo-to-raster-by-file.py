# Name: TopoToRasterByFile_Ex_02.py
# Description: Interpolates a hydrologically correct 
#    surface from point, line, and polygon data using
#    parameters specified in a file.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inParameterFile = "topotorasterbyfile.txt"

# Execute TopoToRasterByFile
outTTRByFile = TopoToRasterByFile(inParameterFile)

# Save the output 
outTTRByFile.save("C:/sapyexamples/output/ttrbyfout02")