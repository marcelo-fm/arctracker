'''****************************************************************************
Name:        Classify Vegetation Points
Description: Classify points representing vegetation with LAS class code values
             of 3, 4, and 5. The code is designed for use as a script tool.
****************************************************************************'''
# Import system modules
import arcpy
import exceptions, sys, traceback

# Set Local Variables
inLas = arcpy.GetParameterAsText(0)
recursion = arcpy.GetParameterAsText(1)
lasd = arcpy.GetParameterAsText(2)
extent = arcpy.GetParameter(3)
calcStats = arcpy.GetParameter(4)

try:
    # Execute CreateLasDataset
    arcpy.management.CreateLasDataset(inLas, lasd, folder_recursion=recursion)
    # Execute ChangeLasClassCodes
    arcpy.ddd.ClassifyLasByHeight(lasd, ground_source='GROUND', 
                                  height_classification=[[3, 5], 
                                                         [4, 17], 
                                                         [5, 120]], 
                                  noise='ALL_NOISE', compute_stats=calcStats, 
                                  extent=extent)

except arcpy.ExecuteError:
    print(arcpy.GetMessages())