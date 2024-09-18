# Name: FeatureToLine_Example2.py
# Description: Use FeatureToLine function to combine features from two 
#                  street feature classes into a single feature class,
#                  then determine an area of impact around all streets
#                  by buffering

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

#  Set local variables
oldStreets = "majorrds.shp"
newStreets = "habitat_analysis.gdb/futrds"
uptodateStreets = "c:/output/output.gdb/allroads"

# Use FeatureToLine function to combine features into single feature class
arcpy.FeatureToLine_management([oldStreets, newStreets], uptodateStreets,
                               "0.001 Meters", "ATTRIBUTES")

# Use Buffer function to determine area of impact around streets
roadsBuffer = "c:/output/output.gdb/buffer_output"
arcpy.Buffer_analysis(uptodateStreets, roadsBuffer, "50 Feet",
                      "FULL", "ROUND", "ALL")