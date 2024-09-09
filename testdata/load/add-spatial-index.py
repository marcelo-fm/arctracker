# Name: AddSpatialIndex_Example2.py
# Description: Add a spatial index to a enterprise geodatabase feature class.

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "c:/Connections/Connection to esoracle.sde"

# Execute AddSpatialIndex
arcpy.AddSpatialIndex_management(in_features)