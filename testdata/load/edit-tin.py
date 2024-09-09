'''****************************************************************************
Name: EditTin Example
Description: This script demonstrates how to use the
             EditTin tool to add features to a output of the CopyTin tool.
****************************************************************************'''

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/LAS"

# Set Local Variables
origTin = "elevation"
copyTin = "elev_copy"
inFCs = [["Clip_Polygon.shp", "<None>", "<None>", "hardclip", False],
         ["new_points.shp", "Shape", "<None>", "masspoints", True]]

# Execute CopyTin
arcpy.ddd.CopyTin(origTin, copyTin, "CURRENT")

# Execute EditTin
arcpy.ddd.EditTin(copyTin, inFCs, Delaunay)