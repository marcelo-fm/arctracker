'''*********************************************************************
Name: TerrainToRaster Example
Description: This script demonstrates how to use the 
             TerrainToRaster tool.
             
**********************************************************************'''
# Import system modules
import arcpy

# Set environment setting
arcpy.env.workspace = "C:/data"

# Set Local Variables
terrain = "sample.gdb/featuredataset/terrain"
bitType = "INT"
method = "LINEAR"
sampling = "CELLSIZE 10"
pyrLvl = 2.5
outRas = arcpy.CreateUniqueName("terrain_level.img")

#Execute TerrainToRaster
arcpy.ddd.TerrainToRaster(terrain, outRas, bitType, 
                          method, sampling, pyrLvl)