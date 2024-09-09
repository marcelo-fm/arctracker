'''****************************************************************************
Name: LandXMLToTin Example
Description: This script demonstrates how to use the
             ListFiles method to collect all LandXML (*.xml) files in a
             workspace as input for the Import3DFiles tool.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"
# Use ListFiles method to grab all xml files (assumedly LandXML files)
landList = arcpy.ListFiles("*.xml")
if landList:
    for landFile in landList:
        # Set Local Variables
        outputFolder = "TINs" # The folder that the TINs will be created in
        outputBase = "Madagascar_" # Base name will be applied to all output TINs
        grab = "1" # TIN selection can be chosen by enumerated values (e.g. 1;2)
        # Execute Import3DFiles
        arcpy.ddd.LandXMLToTin(landFile, outputFolder, outputBase, grab)
        print("Completed creating TIN(s) from {0}.".format(landFile))
else:
    print("There are no xml files in {0}.".format(env.workspace))