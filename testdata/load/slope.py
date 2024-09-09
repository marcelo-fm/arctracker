# Name: Slope_3d_Ex_02.py
# Description: Identifies the rate of maximum change 
#              in z-value from each cell.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
outRaster = "C:/output/outslope02"
outMeasurement = "DEGREE"
zFactor = ""
method = "GEODESIC"
zUnit = "FOOT"

# Check out the ArcGIS 3D Analyst extension license
arcpy.CheckOutExtension("3D")

# Execute Slope
arcpy.ddd.Slope(inRaster, outRaster, outMeasurement, zFactor, method, zUnit)