'''*********************************************************************
Name: Convert Multipatch To Collada
Description: Converts multipatch features in an input workspace 
             to a Collada model.
*********************************************************************'''
# Import system modules
import arcpy

# Script variables
inWorkspace = arcpy.GetParameterAsText(0)

# Set environment settings
arcpy.env.workspace = inWorkspace
# Create list of feature classes in workspace
fcList = arcpy.ListFeatureClasses()

# Determine if the list contained any feature classes
if fcList:
    # Iterate through each feature class
    for fc in fcList:
        # Describe the feature class
        desc = arcpy.Describe(fc)
        # Determine if feature class is a multipatch
        if desc.shapeType is 'MultiPatch':
           # Ensure unique name for output folder
           outDir = arcpy.CreateUniqueName('collada_dir')
           # Specify that collada file is prefixed by source name
           prepend = 'PREPEND_SOURCE_NAME'
           # Specify the feature attribute used to name Collada files
           fldName = 'OID'
           # Run MultipatchToCollada
           arcpy.conversion.MultipatchToCollada(fc, outDir, prepend, fldName)
else:
    print('There are no feature classes in {0}.'.format(inWorkspace))