# Name: RemoveSpatialIndex_Example2.py
# Description: Removes a spatial index from a SDE feature class.

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "c:/Connections/Connection to esoracle.sde"

# Set local variables
in_features = "LPI.Land/LPI.PLSSFirstDivision"

# Execute RemoveSpatialIndex
arcpy.RemoveSpatialIndex_management(in_features)