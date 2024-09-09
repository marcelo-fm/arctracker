#-------------------------------------------------------------------------------
# Name: CreateBuffers.py
# Description: Buffer damaged building by 300 meters

# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/DamageSurvey.gdb"

# Set local variables
inFeatures = "DamageAssessment"
out = "DangerousAreas"

# Run Create Buffers
arcpy.gapro.CreateBuffers(inFeatures, out, "GEODESIC", "DISTANCE", 
                          None, "300 Meters", None, "ALL", None, None, 
                          "SINGLE_PART")