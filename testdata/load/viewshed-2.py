# Name: Viewshed2_Ex_02.py
# Description: Determines the raster surface locations visible to a set of
#              observer features.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# set local variables
inRaster = "elevation"
inObservers = "obser2.shp"
outAGL = ""
analysisType = "OBSERVERS"
verticalError = ""
outAnalysisRelationTable = "C:/sapyexamples/output/obser_region2.dbf"
refractCoeff = ""
surfaceOffset = "offsetb"
observerElevation = "spot"
observerOffset = "offseta"
innerRadius = "radius1"
innerIs3D = "False"
outerRadius = "radius2"
outerIs3D = "True"
horizStartAngle = "azimuth1"
horizEndAngle = "azimuth2"
vertUpperAngle = "vert1"
vertLowerAngle = "vert2"
analysisMethod = "ALL_SIGHTLINES"

# Execute Viewshed2
outViewshed2 = Viewshed2(inRaster, inObservers, outAGL, analysisType,
                         verticalError, outAnalysisRelationTable, refractCoeff,
                         surfaceOffset, observerElevation, observerOffset,
                         innerRadius, innerIs3D, outerRadius, outerIs3D,
                         horizStartAngle, horizEndAngle, vertUpperAngle,
                         vertLowerAngle, analysisMethod)

# Save the output
outViewshed2.save("C:/sapyexamples/output/outvwshd2_02")