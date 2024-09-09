# Name: RegisterAsVersioned_Example.py
# Description: Registers dataset as versioned

# Import system modules
import arcpy

# Set local variables
datasetName = "c:/Connections/ninefour@gdb.sde/ninefour.GDB.ctgFuseFeature"

# Run RegisterAsVersioned
arcpy.management.RegisterAsVersioned(datasetName, "NO_EDITS_TO_BASE")