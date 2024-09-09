# Name: InverseDistanceWeighting_Example_02.py
# Description: Interpolate a series of point features onto a rectangular raster
#              using Inverse Distance Weighting (IDW).
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "OZONE"
outLayer = "outIDW"
outRaster = "C:/gapyexamples/output/idwout"
cellSize = 2000.0
power = 2

# Set variables for search neighborhood
majSemiaxis = 300000
minSemiaxis = 300000
angle = 0
maxNeighbors = 15
minNeighbors = 10
sectorType = "ONE_SECTOR"
searchNeighbourhood = arcpy.SearchNeighborhoodStandard(majSemiaxis, minSemiaxis,
                                                       angle, maxNeighbors,
                                                       minNeighbors, sectorType)

# Execute IDW
arcpy.IDW_ga(inPointFeatures, zField, outLayer, outRaster, cellSize, 
             power, searchNeighbourhood)