#---------------------------------------------------------------------------
# Name: CreateViewshed_example02.py
# Description: Creates a viewshed image service raster from given surface
#   and observer points.
#
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inSurface = "https://myserver/rest/services/elevation/ImageServer"
inObservers = "https://myserver/rest/services/destination/FeatureServer/0"
outputViewshed = "outview1"
optimizeFor = "Speed"
maxDistType = "Distance"
maxDist = "9 Miles"
maxDistField = "#"
minDistType = "Distance"
minDist = "0 Miles"
minDistField = "#"
distanceIs3D = "2D"
obsElevationType = "Elevation"
obsElevation = "#"
obsElevationField = "#"
obsOffsetType = "Height"
obsOffset = "6 Feet"
obsOffsetField = "#"
surfOffsetType = "Height"
surfOffset = "3 Feet"
surfOffsetField = "#"
outputAgl = "outagl1"

# Execute Create Viewshed raster analysis tool
arcpy.ra.CreateViewshed(
    inSurface, inObservers, outputViewshed, optimizeFor,
    maxDistType, maxDist, maxDistField, minDistType, minDist,
    minDistField, distanceIs3D, obsElevationType, obsElevation,
    obsElevationField, obsOffsetType, obsOffset, obsOffsetField,
    surfOffsetType, surfOffset, surfOffsetField, outputAgl)