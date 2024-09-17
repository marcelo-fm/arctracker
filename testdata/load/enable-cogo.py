import arcpy

# Variable to contain the path of the feature class that is to be COGO enabled
lineFeatureClass = r"d:\test.gdb\myLineFC"

# Check to see if the feature class is already enabled by using .isCOGOEnabled on a Describe
if arcpy.Describe(lineFeatureClass).isCOGOEnabled == False:
    # If it returns False, run EnableCOGO_management and pass the feature class
    arcpy.EnableCOGO_management(lineFeatureClass)
else:
    print("{} is already COGO Enabled".format(lineFeatureClass))