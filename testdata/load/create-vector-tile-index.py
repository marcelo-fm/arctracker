# Name: CreateVectorTileIndex.py
# Description: Find all the maps in the project and
#   create vector tile index polygon feature class for each map

# import system modules
import os
import arcpy

#set environment settings
arcpy.env.overwriteOutput = True
outputPath = "C://Tilepackages//"

# Loop through the project, find all the maps, and
#   creates vector tile index polygon for each map,
#   using the same name as the map

p = arcpy.mp.ArcGISProject("c:\\temp\\myproject.aprx")for m in p.listMaps():
      print("Creating Vector Tile Index for: " + m.name)
      arcpy.CreateVectorTileIndex_management(m, outputPath + m.name + '.shp', "ONLINE", "", 10000)