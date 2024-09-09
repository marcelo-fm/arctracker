# Name: ExtentCreation.py

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:\data\City.gdb"
arcpy.env.outputCoordinateSystem = arcpy.Describe("roads").spatialReference

# Set local variables
in_features = "roads"

# Generate the extent coordinates using CalculateGeometry
arcpy.management.CalculateGeometryAttributes(in_features, [["Left", "EXTENT_MIN_X"],
                                                           ["Bottom", "EXTENT_MIN_Y"],
                                                           ["Right", "EXTENT_MAX_X"],
                                                           ["Top", "EXTENT_MAX_Y"]])