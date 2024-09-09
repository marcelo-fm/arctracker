'''****************************************************************************
Name: ReplaceTerrainPoints Example
Description: This script demonstrates how to use the 
             ReplaceTerrainPoints tool.
****************************************************************************'''

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set Local Variables
InTerrain = "sample.gdb/featuredataset/terrain"
TerrainFCl = "points_old"
InPoints = "sample.gdb/featuredataset/terrain/pts_new"

#Execute ReplaceTerrainPoints
arcpy.ddd.ReplaceTerrainPoints(InTerrain, TerrainFCl, InPoints)