#-------------------------------------------------------------------------------
# Name: InterpolatePoints_example02.py
# Description: Interpolates a point feature service into an image service raster.
#
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inPoints = 'https://MyPortal.esri.com/server/rest/services/Hosted/myPoints/FeatureServer/0'
inField = 'myField'
outRaster = 'outImgServ'
optimizeFor = 'SPEED'
transform = 'False'
subsetSize = 50
numNeighbors = 8
outCellSize = '10000 Meters'
error = 'NO_OUTPUT_ERROR'

# Execute InterpolatePoints
arcpy.ra.InterpolatePoints(inPoints, inField, outRaster, optimizeFor, transform, 
                           subsetSize, numNeighbors, outCellSize, error)