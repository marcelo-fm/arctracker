# Name: UnregisterAsVersioned_Example.py
# Description: Unregisters a dataset as versioned
# Author: ESRI

# Import system modules
import arcpy

# Set local variables
datasetName = "c:/whistler@prod.sde/prod.GDB.ctgFuseFeature"

# Execute UnregisterAsVersioned
arcpy.UnregisterAsVersioned_management(datasetName,
                                       "NO_KEEP_EDIT",
                                       "COMPRESS_DEFAULT")