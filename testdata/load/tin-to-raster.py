'''******************************************************************
Name: TinRaster Example
Description: This script demonstrates how to use the 
             TinRaster tool to create rasters from 
             each TIN in the target workspace.
******************************************************************'''
# Import system modules
import arcpy

# Set environment setting
arcpy.env.workspace = "C:/data"

# Set Local Variables
dataType = "INT"
method = "NATURAL_NEIGHBORS"
sampling = "CELLSIZE 10"
zfactor = "1"

# Create list of TINs
TINList = arcpy.ListDatasets("*", "Tin")

# Verify the presence of TINs in the list
if TINList:
    # Iterate through the list of TINs
    for dataset in TINList:
        # Define the name of the output file
        outRaster = "{0}_natural.img".format(dataset)
        # Execute TinRaster
        arcpy.ddd.TinRaster(dataset, outRaster, dataType, 
                            method, sampling, zfactor)
    print("Finished.")
else:
    print("There are no TIN(s) in {0}.".format(env.workspace))