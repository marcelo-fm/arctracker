'''****************************************************************************
Name: Skyline Example
Description: This script demonstrates how to use the 
             Skyline tool.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'

# Set Local Variables
inPts = "observers.shp"

# Make sure output has a unique name
outFC = arcpy.CreateUniqueName("skyline_output.shp")
inSurface = "sample.gdb/featuredataset/terrain"
obstructionFCs = "buildings.shp; billboards.shp"
surfRad = "1000 meters"
surfElev = "100 meters"
LOD = "FULL_DETAIL"
fromAzim = 0
toAzim = 360
incAzim = 1
maxHorizRad = 0
segSky = "SEGMENT_SKYLINE"
scale = 100
scaleAcc = "ELEVATION"
scaleMethod = "SKYLINE_MAXIMUM"

# Execute Skyline
arcpy.ddd.Skyline(inPts, outFC, inSurface, surfRad, surfElev, 
                  obstructionFCs, LOD, fromAzim, toAzim, incAzim, 
                  maxHorizRad, segSky, scale, scaleAcc, scaleMethod)