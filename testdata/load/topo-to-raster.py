# Name: TopoToRaster_3D_Ex_02.py
# Description: Interpolates a hydrologically correct surface 
#              from point, line, and polygon data.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPointElevations = "C:/data/spots.shp spot_meters PointElevation"
inContours = "C:/data/contours.shp spot_meters Contour"
inFeatures = (inPointElevations + ";" + inContours)
outRaster = "C:/output/topoout"


# Execute TopoToRaster
arcpy.ddd.TopoToRaster(inFeatures, outRaster)