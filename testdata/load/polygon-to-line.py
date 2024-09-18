# Name: PolygonToLine_Example2.py
# Description: Use PolygonToLine function to convert polygons to lines,
#              and report how many shared or overlapping boundary lines
#              were found.

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/landcovers.gdb"
 
# Create variables for the input and output feature classes
inFeatureClass = "bldgs"
outFeatureClass = "bldgs_lines"
 
# Run PolygonToLine to convert polygons to lines using default neighbor_option
arcpy.PolygonToLine_management(inFeatureClass, outFeatureClass)

# Select lines that have LEFT_FID values greater than -1
arcpy.MakeFeatureLayer_management(outFeatureClass, "selection_lyr", 
                                  "\"LEFT_FID\" > -1")
result = arcpy.GetCount_management("selection_lyr")

if result[0] == "0":
    print("No overlapping or shared boundary lines were found.")
else:
    print("{} overlapping or shared boundary lines were found.".format(result[0]))