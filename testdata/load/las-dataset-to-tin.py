'''**********************************************************************
Name: LAS Dataset to TIN Example
Description: Create a TIN using bare earth lidar measurements. This
             script is designed for use as a script tool.
**********************************************************************'''
# Import system modules
import arcpy

# Set Local Variables
lasD = arcpy.GetParameterAsText(0)
inLas = arcpy.GetParameterAsText(1) #input las files
surfCons = arcpy.GetParameterAsText(2) #input surface constraints
sr = arcpy.GetParameter(3) #spatial reference of las dataset
outTin = arcpy.GetParameterAsText(4)
thinningType = arcpy.GetParameterAsText(5)
thinningMethod = arcpy.GetParameterAsText(6)
thinningValue = arcpy.GetParameter(7)
zFactor = arcpy.GetParameter(8)

# Execute CreateLasDataset
arcpy.management.CreateLasDataset(inLas, lasD, 'RECURSION', surfCons, sr)
lasLyr = arcpy.CreateUniqueName('lasdToTin', 'in_memory')
classCode = 2
returnValue = 'LAST'
# Execute MakeLasDatasetLayer
arcpy.management.MakeLasDatasetLayer(lasD, lasLyr, classCode, returnValue)
# Define extent of the area of interest
env.extent(1426057, 606477, 1449836, 623246)
# Execute LasDatasetToTin
arcpy.ddd.LasDatasetToTin(lasLyr, outTin, thinningType,
                          thinningMethod, thinningValue, zFactor)