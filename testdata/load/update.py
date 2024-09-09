# Name: UpdateZones.py
# Purpose: Update the "lots" feature class with features from "cutzones"

# Import system modules
import arcpy
 
# Set the workspace
arcpy.env.workspace = "c:/data/city.gdb"

# Set local parameters
inFeatures = "lots"
updateFeatures = "cutzones"
outFeatures = "futurecut"

# Process: Update
arcpy.analysis.Update(inFeatures, updateFeatures, outFeatures, "NO_BORDERS")