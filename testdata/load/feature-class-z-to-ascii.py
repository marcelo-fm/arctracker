'''****************************************************************************
Name: FeatureClassZToASCII Example
Description: This script demonstrates how to use the
             FeatureClassZToASCII tool to create generate files for all
             z-aware point features in a given workspace.
****************************************************************************'''
import arcpy

try:
    # Set environment settings
    arcpy.env.workspace = 'C:/data'
    # List all points in the target workspace
    fcList = arcpy.ListFeatureClasses("*", "POINT")
    if fcList:
        # Set Local Variables
        outFolder = "C:/output"
        outFormat = "GENERATE"
        delimeter = "SPACE"
        decimal = "FIXED"
        digits = 3
        dec_sep = "DECIMAL_POINT"
        for fc in fcList:
            # Use Describe method to evaluate whether the feature class is z-aware
            desc = arcpy.Describe(fc)
            if desc.hasZ == True:
                # Define the output file name by replacing '.shp' with _ascii.txt
                outName = fc.replace('.shp', '') + "_ascii.txt"
                #Execute FeatureClassZToASCII_3d
                arcpy.ddd.FeatureClassZToASCII(fc, outFolder, outName, outFormat, delimeter, decimal, digits, dec_sep)
    else:
        print("There are no feature classes in the " + env.workspace + " directory.")

except arcpy.ExecuteError:
    print(arcpy.GetMessages())
except Exception as err:
    print(err)