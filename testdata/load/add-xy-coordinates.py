# Name: AddXY_Example2.py
# Description: Adding XY points to the climate dataset

# Import system modules
import arcpy
from arcpy import env

# Set workspace
env.workspace = "C:/data"

# Set local variables
in_data= "climate.shp"
in_features = "climateXPpts2.shp"

# Copying data to preserve original dataset
# Execute Copy
arcpy.Copy_management(in_data, in_features)

# Execute AddXY
arcpy.AddXY_management(in_features)