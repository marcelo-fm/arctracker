'''*********************************************************************
Name: AddSurfaceInformation Example
Description: This script demonstrates how to use AddSurfaceInformation 
             on all 2D feature classes in a target workspace.
*********************************************************************'''
# Import system modules
import arcpy

# Set Local Variables
arcpy.env.workspace = 'c:/data'
inSurface = 'fgdb.gdb/municipal/terrain'
pyramid = 5
method = "BILINEAR"

# Create list of feature classes
fcList = arcpy.ListFeatureClasses()

if fcList:
    for fc in fcList:
        desc = arcpy.Describe(fc)
        # Determine if the feature is 2D
        if not desc.hasZ:
            if desc.shapeType == "Polygon":
                # Desired properties separated by semi-colons
                Prop = "Z_MIN;Z_MAX" 
            elif desc.shapeType == "Point":
                Prop = "Z"
            elif desc.shapeType == "Multipoint":
                Prop = "Z_MIN;Z_MAX;Z_MEAN"
            elif desc.shapeType == "Polyline":
                Prop = "LENGTH_3D"
            # Execute AddSurfaceInformation
            arcpy.ddd.AddSurfaceInformation(fc, inSurface, Prop, 
                                            method, 15, 1, pyramid)
            print("Completed adding surface information.")