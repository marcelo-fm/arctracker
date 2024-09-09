# Name: calculategridconvergenceangle_example.py
# Description: Calculates the true north rotation angle for features

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:\Data\ProjectData.gdb"

# Set local variables
inFeatures = "US_states"
angleField = "angle"
rotationMethod = "GEOGRAPHIC"
coordSystemField = "UTM"

# Execute CalculateGridConvergenceAngle
arcpy.CalculateGridConvergenceAngle_cartography(inFeatures, angleField,
                                                rotationMethod,
                                                coordSystemField)