'''*****************************************************************
Name: TerrainToPoints Example
Description: This script demonstrates how to use the 
             TerrainToPoints tool.
*****************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set Local Variables
terrain = "sample.gdb/featuredataset/terrain"
outPts = arcpy.CreateUniqueName("terrain_pts", "sample.gdb")
outGeo = "POINT"

# Execute TerrainToPoints
arcpy.ddd.TerrainToPoints(terrain, outPts, 6, "<NONE>", outGeo)