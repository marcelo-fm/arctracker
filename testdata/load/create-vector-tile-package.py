# Name: CreateVectorTilePackage.py
# Description: Find all the maps in the project and
#   create a vector tile package for each map
# import system modules
import os
import arcpy

#set environment settings
arcpy.env.overwriteOutput = True
outputPath = "C://Tilepackages//"

# Loop through the project, find all the maps, and
#   create a vector tile package for each map,
#   using the same name as the map
p = arcpy.mp.ArcGISProject("c:\\temp\\myproject.aprx")
for m in p.listMaps():
    print("Packaging " + m.name)
    arcpy.CreateVectorTilePackage_management(m, outputPath + m.name + '.vtpk', "ONLINE", "", "INDEXED", 295828763.795777, 564.248588)