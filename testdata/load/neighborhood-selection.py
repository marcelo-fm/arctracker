# Name: NeighborhoodSelection_Example_02.py
# Description: Creates a layer of points based on a user-defined neighborhood.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPoints = "ca_ozone_pts.shp"
outLayer = "outNS"
pointCoord = "-2000000 -50000"
maxNeighbors = 20
minNeighbors = 5
majSemiaxis = 200000
minSemiaxis = 200000
angle = 0
shape = "One Sector"

# Execute NeighborhoodSelection
arcpy.GANeighborhoodSelection_ga(inPoints, outLayer, pointCoord, maxNeighbors,
                                 minNeighbors, majSemiaxis, minSemiaxis, angle,
                                 shape)