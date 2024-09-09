'''****************************************************************************
Name: Layer3DToFeatureClass Example
Description: This script demonstrates how to use the
             Layer3DToFeatureClass tool to create multipatches from all
             layers in a target workspace. The layer files are assumed to have
             been saved wtih 3D rendering from ArcScene.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Use the ListFiles method to identify all layer files in workspace
if arcpy.ListFiles("*.lyr"):
    for lyrFile in arcpy.ListFiles("*.lyr"):
        # Set Local Variables
        outFC = "Test.gdb/{0}".format(lyrFile[:-4]) #Strips '.lyr' from name
        #Execute Layer3DToFeatureClass
        arcpy.Layer3DToFeatureClass_3d(file, outFC)
else:
    print("There are no layer files in {0}.".format(env.workspace))