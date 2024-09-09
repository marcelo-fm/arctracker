# Name: BufferZones.py
# Purpose: Simplify features using the Generalize tool and then Buffer them

# Import script modules
import arcpy

# Set the workspace
arcpy.env.workspace = "C:/data/data.gdb"

# Set local parameters
inFeatures = "zones"
gTolerance = "4 Feet"
copFeatures = "zones_cp"
bufDist = "50 Miles"
bufOutput = "zones_buff"

# Since Generalize permanently updates the input, first make a copy of the 
# original feature class
arcpy.management.CopyFeatures(inFeatures, copFeatures)

# Use the Generalize tool to simplify the Buffer input to shorten Buffer 
# processing time
arcpy.edit.Generalize(copFeatures, gTolerance)

# Buffer the output
arcpy.analysis.Buffer(copFeatures, bufOutput, bufDist)