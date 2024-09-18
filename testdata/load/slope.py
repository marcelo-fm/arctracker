# Name: _Ex_02.py
# Description: Identifies slope from each cell.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
outMeasurement = "DEGREE"
zFactor = ""
method = "GEODESIC"
zUnit = "FOOT"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute Slope
outSlope = Slope(inRaster, outMeasurement, zFactor, method, zUnit)

# Save the output 
outSlope.save("C:/sapyexamples/output/outslope02")