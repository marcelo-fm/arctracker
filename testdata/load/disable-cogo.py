import arcpy

#Variable to contain the path of the feature class that will have COGO disabled
lineFeatureClass = r"d:\test.gdb\myLineFC"

#Check to see if the feature class is already COGO enabled by using .isCOGOEnabled on a Describe
if arcpy.Describe(lineFeatureClass).isCOGOEnabled == True:
    #If it returns True, run DisableCOGO_management and pass the feature class
    arcpy.DisableCOGO_management(lineFeatureClass)
else:
    print("{} is not COGO Enabled".format(lineFeatureClass))