'''****************************************************************************
Name: PointFileInformation Example
Description: This script demonstrates how to use the 
             PointFileInformation tool to create an output file that contains
             all LAS files under a parent folder.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"
lidarList = arcpy.ListFiles("*.las")
if lidarList:
    # Set Local Variables
    outputFC = "Test.gdb/output_las_info"
    prj = "Coordinate Systems/Geographic Coordinate Systems/World/WGS 1984.prj"
    extrudeGeom = True # Indicates whether to create extruded geometry shapes
    sumClass = True # Indicates whether to summarize output by class code
    decSep = "DECIMAL_POINT" # Identifies the decimal separator
    
    #Execute PointFileInformation
    arcpy.ddd.PointFileInformation(lidarList, outputFC, "LAS", "las", prj, 
                                "", extrudeGeom, decSep, sumClass)
    print("Finished executing Point File Information.")
else:
    print("There are no LAS files in {0}.".format(env.workspace))