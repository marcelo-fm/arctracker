# Name: Flipline_Example.py
# Description: Flip line features

import arcpy
arcpy.env.workspace = "C:/data/project.gdb"

inFeatures = "streams"

arcpy.edit.FlipLine(inFeatures)