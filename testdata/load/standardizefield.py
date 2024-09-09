# Import system modules
import arcpy

try:
    # Set the workspace and input features.
    arcpy.env.workspace = r"C:\\Standardize\\MyData.gdb"
    inputFeatures = ”County_VoterTurnout”

    # Set the input fields that will be standardized
    fields = "votes_total;rawdiff_dem_vs_gop;pctdiff_dem_vs_gop"

    # Set the standardization method.
    method = "ROBUST"

    # Run the Standardize Field tool
    arcpy.management.StandardizeField(inputFeatures, fields, method)

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message.
    print(arcpy.GetMessages())