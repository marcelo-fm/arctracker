'''****************************************************************************
Name: Skyline Barrier Example
Description: This script demonstrates how to use the 
             Skyline Barrier tool.

****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'
# Set Local Variables
inPts = 'observers.shp'
inLine = 'skyline.shp'
outFC = 'output_barriers.shp'
minRadius = '0 METERS'
maxRadius = '200 METERS'

#Execute SkylineBarrier
arcpy.ddd.SkylineBarrier(inPts, inLine, outFC, minRadius,
                      maxRadius, 'CLOSED')