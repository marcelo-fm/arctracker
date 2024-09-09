# Name: RadialBasisFunctions_Example_02.py
# Description: RBF methods are a series of exact interpolation techniques;
#              that is, the surface must go through each measured sample value.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "OZONE"
outLayer = "outRBF"
outRaster = "C:/gapyexamples/output/rbfout"
cellSize = 2000.0
rbf = "THIN_PLATE_SPLINE"
smallscaleParam = ""

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

# Execute RadialBasisFunctions
arcpy.RadialBasisFunctions_ga(inPointFeatures, zField, outLayer, outRaster, 
                              cellSize, searchNeighbourhood, rbf, smallscaleParam)