# Name: CreateFishnet.py
# Description: Creates rectangular cells

# import system module
import arcpy
from arcpy import env

# set workspace environment
env.workspace = "C:/data/output"

# Set coordinate system of the output fishnet
env.outputCoordinateSystem = arcpy.SpatialReference("NAD 1983 UTM Zone 11N")

outFeatureClass = "fishnet10by10.shp"

# Set the origin of the fishnet
originCoordinate = '1037.26 4145.81'

# Set the orientation
yAxisCoordinate = '1037.26 4155.81'

# Enter 0 for width and height - these values will be calcualted by the tool
cellSizeWidth = '0'
cellSizeHeight = '0'

# Number of rows and columns together with origin and opposite corner 
# determine the size of each cell 
numRows =  '10'
numColumns = '10'

oppositeCoorner = '19273.61 18471.17'

# Create a point label feature class 
labels = 'LABELS'

# Extent is set by origin and opposite corner - no need to use a template fc
templateExtent = '#'

# Each output cell will be a polygon
geometryType = 'POLYGON'

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate, cellSizeWidth, cellSizeHeight, numRows, numColumns, oppositeCoorner, labels, templateExtent, geometryType)