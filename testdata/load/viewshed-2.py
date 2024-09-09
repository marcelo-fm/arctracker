# Name: Viewshed_3d_Ex_02.py
# Description: Determines the raster surface locations visible to a set of
#              observer features.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"


parmSurface = "elevation"
parmObservers = "obser2.shp"
parmOutput = "c:/output/outvshd02"
parmAGL = ""
parmAnalysisType="OBSERVERS"
parmVerticalError = ""
parmAnalysisRelationTable = "C:/output/obser_region2.dbf"
parmRefractCoeff = ""
parmSurfaceOffset = "offsetb"
parmObserverElevation="spot"
parm_ObserverOffset="offseta"
parmInnerRadius = "radius1"
parmInnerIs3D="False"
parmOuterRadius = "radius2"
parmOuterIs3D="True"
parmAz1 = "azimuth1"
parmAz2 = "azimuth2"
parmVert1 = "vert1"
parmVert2 = "vert2"

# Execute Viewshed2
result = arcpy.Viewshed2_3d(parmSurface, parmObservers, parmOutput, parmAGL,
parmAnalysisType, parmVerticalError, parmAnalysisRelationTable,
parmRefractCoeff, parmSurfaceOffset, parmObserverElevation,
parm_ObserverOffset,parmInnerRadius, parmInnerIs3D, parmOuterRadius,
parmOuterIs3D, parmAz1, parmAz2, parmVert1, parmVert2)