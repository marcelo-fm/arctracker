# Name: TopoToRasterByFile_3d_Ex_02.py
# Description: Interpolates a hydrologically correct surface from 
#    point, line, and polygon data using parameters specified in a file.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inParameterFile = "topotorasterbyfile.txt"
outRaster =  "C:/output/ttrbyfout02"

# Execute TopoToRasterByFile
arcpy.ddd.TopoToRasterByFile(inParameterFile, outRaster)