# Name: SurfaceParameters_Ex_03.py
# Description: Derive aspect for an elevation surface over a distance of 5m, correct
# for direction distortion from non-conformal projection system. 
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy.ddd import *

# Set environment settings
arcpy.env.workspace = "C:/data"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("3D")

# Set local variables
inRaster = "elevation_1m.tif"
outRaster = "C:/data/output/outsurfaceparameters03.tif"
inParameterType = "ASPECT"
inNeighborhoodDistance = "5 METERS"
inProjectGeodesicAzimuths = "PROJECT_GEODESIC_AZIMUTHS"

# Execute the tool
SurfaceParameters(inRaster, outRaster, inParameterType, "", inNeighborhoodDistance,
                  "", "", "", inProjectGeodesicAzimuths)