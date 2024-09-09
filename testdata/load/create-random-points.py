# Name: RandomPoints.py
# Purpose: create several types of random points feature classes

# Import system modules
import arcpy

# set environment settings
arcpy.env.overwriteOutput = True

# Create random points in an extent defined simply by numbers
outFolder = "C:/data"
numExtent = "0 0 1000 1000"
numPoints = 100
outName = "myRandPnts.shp"
arcpy.env.outputCoordinateSystem = "Coordinate Systems/Projected Coordinate Systems/World/Miller Cylindrical (world).prj"
arcpy.management.CreateRandomPoints(outFolder, outName, "", numExtent, numPoints)
arcpy.env.outputCoordinateSystem = ""
 
# Create random points in an extent defined by another feature class
outName = "testpoints.shp"
fcExtent = "C:/data/studyarea.shp"
arcpy.management.CreateRandomPoints(outFolder, outName, "", fcExtent, numPoints)
 
# Create random points in the features of a constraining feature class
# Number of points for each feature determined by the value in the field specified
outGDB = "C:/data/county.gdb"
outName = "randpeople"
conFC = "C:/data/county.gdb/blocks"
numField = "POP2000"
arcpy.management.CreateRandomPoints(outGDB, outName, conFC, "", numField)

# Create random points in the features of a constraining 
# Feature class with a minimum allowed distance
outName = "constparcelpnts"
conFC = "C:/data/county.gdb/parcels"
numPoints = 10
minDistance = "5 Feet"
arcpy.management.CreateRandomPoints(outGDB, outName, conFC, "", numPoints, 
                                    minDistance) 

# Create random points with a multipoint output
outName = "randomMPs"
fcExtent = "C:/data/county.gdb/county"
numPoints = 100
numMP = 10
arcpy.management.CreateRandomPoints(outGDB, outName, "", fcExtent, numPoints, 
                                    "", "MULTIPOINT", numMP)