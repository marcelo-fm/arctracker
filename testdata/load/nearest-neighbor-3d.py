# Name: NearestNeighbor3D_Example_02.py
# Description: Creates a voxel layer source file from 3D categorical points.
# Requirements: Geostatistical Analyst Extension
# Author: Esri


# Create a voxel layer source file of 3D soil class points within a field
# and between a bedrock layer and the ground.



# Import system modules
import arcpy

# Allow overwriting output
arcpy.env.overwriteOutput = True

# Define 3D input points with categories
in3DPoints = "C:/gapydata/inputs.gdb/my3DSoilPoints"
categoryField = "SoilClass"
outNetCDF = "C:/gapydata/outputs/SoilClassVoxel.nc"

# Define voxel dimensions and elevation inflation
xSpacing = "50 Meters"
ySpacing = "50 Meters"
elevSpacing = "5 Meters"
elevInflation = 1

# Define study area, bedrock elevation layer, and ground elevation layer
studyArea = "C:/gapydata/inputs.gdb/StudyAreaPolygon"
minElevRaster = "C:/gapydata/inputs.gdb/BedrockDepth"
maxElevRaster = "C:/gapydata/inputs.gdb/WorldElevationDEM"


# Check out the ArcGIS Geostatistical Analyst extension license
arcpy.CheckOutExtension("GeoStats")

# Execute Nearest Neighbor 3D
arcpy.ga.NearestNeighbor3D(in3DPoints, categoryField,outNetCDF,
                           xSpacing, ySpacing, elevSpacing,
                           elevInflation, studyArea, minElevRaster,
                           maxElevRaster)