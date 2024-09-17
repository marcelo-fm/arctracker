# Name: SplitLine_Example2.py
# Description: Split a bus line feature at its vertices (bus stops)
#              and find a midpoint of each new line for further analysis.
 
# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"
 
# Set local variables
inFeatures = "buslines.shp"
outFeatureClass = "c:/output/output.gdb/buslines_segments"
midPtsFeatureClass = "c:/output/output.gdb/buslines_segments_midPts"

# Run SplitLine to get new lines, each of which is between two bus stops
arcpy.management.SplitLine(inFeatures, outFeatureClass)

# Run FeatureVerticesToPoints to find a midpoint for every new line
arcpy.management.FeatureVerticesToPoints(outFeatureClass,
                                         midPtsFeatureClass, "MID")

# Comments: You can add attribute information, such as driving time,
#           to the midpoint feature class and display the attributes 
#           as an alternative label for each line between two bus stops.