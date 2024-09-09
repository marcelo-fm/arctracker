'''*********************************************************************
Name: TerrainToTin Example
Description: This script demonstrates how to use the 
             TerrainToTin tool.
**********************************************************************'''

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set Local Variables
inTerrain = "sample.gdb/featuredataset/terrain"
pyrRes = 6
maxNodes = 5000000
clipExtent = False
# Ensure output name is unique
outTIN = arcpy.CreateUniqueName("tin")

#Execute TerrainToTin
arcpy.ddd.TerrainToTin(inTerrain, outTIN, pyrRes, maxNodes, clipExtent)
    
del arcpy