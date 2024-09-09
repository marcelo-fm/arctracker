'''****************************************************************************
Name: MultiPatchFootprint Example
Description: Creates footprint polygons for all multipatches in a workspace.
****************************************************************************'''
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'
fcList = arcpy.ListFeatureClasses()
if fcList:
    for fc in fcList:
        # Determine if the feature class is a multipatch
        desc = arcpy.Describe(fc)
        if desc.shapeType is "MultiPatch":
            outPoly = "{0}_Footprint.shp".format(desc.baseName)
            #Execute MultiPatchFootprint
            arcpy.ddd.MultiPatchFootprint(fc, outPoly)