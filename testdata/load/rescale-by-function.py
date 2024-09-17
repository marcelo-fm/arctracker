# Name: TfMSSmall_Ex_02.py
# Description: Rescales input raster data using a MSSmall function and
#     transforms the function values onto a specified evaluation scale. 
# Requirements: Spatial Analyst Extension
# Author: esri

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Create the TfMSSmall object
meanmult = 1.25
stdmult = 1.5
lowerthresh = "#"
valbelowthresh = "10"
upperthresh = 4000
valabovethresh = "NoData"
myTfFunction = TfMSSmall(meanmult, stdmult, lowerthresh, valbelowthresh, upperthresh, valabovethresh)

# Set evaluation scale
fromscale = 1
toscale = 10

# Execute RescaleByFunction
outRescale = RescaleByFunction(inRaster, myTfFunction, fromscale, toscale)

# Save the output
outRescale.save("c:/sapyexamples/rescaletfms2")