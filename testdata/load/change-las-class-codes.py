'''****************************************************************************
Name: Update LAS 1.0 Classification to ASPRS 1.1 Specs
Description: Updates classification of version 1.0 LAS files to conform to
             the standardized class codes introduced in the 1.1 specifications.
             The code is designed for use as a script tool.
****************************************************************************'''
# Import system modules
import arcpy

# Set Local Variables
inLas = arcpy.GetParameterAsText(0)
recursion = arcpy.GetParameterAsText(1)
lasd = arcpy.GetParameterAsText(2)
reclassList = arcpy.GetParameterAsText(3) #List of values '<oldCode> <newCode>'
calcStats = arcpy.GetParameter(4)

# Execute CreateLasDataset
arcpy.management.CreateLasDataset(inLas, lasd, recursion)
# Execute ChangeLasClassCodes
arcpy.ddd.ChangeLasClassCodes(lasd, reclassList, calcStats)