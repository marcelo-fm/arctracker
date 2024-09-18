# Name: CreateMapTilePackage.py
# Description: Create multiple map tile packages for a given map

# import system modules
import os
import arcpy

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Data\MinMaxLOD\states73K"

# Create multiple map tile packages for given map,

aprx = arcpy.mp.ArcGISProject("c:\\temp\\myproject.aprx")
map1 = aprx.listMaps()[0]
extent = ""
aoi = ""
createMultiplePackages = "create_multiple_packages"
outputFolder = r"C:\11\multi"

arcpy.management.CreateMapTilePackage(map1, "ONLINE", "", "PNG", 9, None, "MapSummary", "MapTag",
                                      extent, "", "tpkx", 5, aoi,createMultiplePackages, outputFolder )