'''****************************************************************************
Name: RemoveFeatureClassFromTerrain Example
Description: This script demonstrates how to use the 
             RemoveFeatureClassFromTerrain tool.
****************************************************************************'''

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set Local Variables
inTerrain = "sample.gdb/featuredataset/terrain"
remFC = "points_1995"
#Execute RemoveFeatureClassFromTerrain
arcpy.ddd.RemoveFeatureClassFromTerrain(inTerrain, remFC)