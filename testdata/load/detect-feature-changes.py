# Name:        DetectFeatureChanges_example_script2.py
# Description: Perform change detection between newly received road data and
#              existing road data and find the number of new roads and the
#              total length of them.
# Author:      Esri
# -----------------------------------------------------------------------

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.overwriteOutput = True
env.workspace = r"D:\conflationTools\ScriptExamples\data.gdb"

# Set local variables
updateFeatures = "updateRoads"
baseFeatures = "baseRoads"
dfcOutput = "dfc_out"

search_distance = "300 Feet"
match_fields = "RD_NAME FULLNAME"

statsTable = "new_roads_stats"

# Perform spatial change detection
arcpy.DetectFeatureChanges_management(updateFeatures, baseFeatures, dfcOutput, search_distance, match_fields)

# ====================================================================================
# Note 1:  The result of DetectFeatureChanges may contain errors; see tool reference.
#          Inspection and editing may be necessary to ensure correct CHANGE_TYPE N, which
#          represents un-matched update feautres, before further calculations.
#
#          One of the quick ways of checking whether the CHANGE_TYPE N features have
#          matching base features is to find their mid-points and use them to search for
#          features in base data, as processed below.
# ====================================================================================

# ======== Check update roads with CHANGE_TYPE N for potential match
# Make Feature Layer with selection of CHANGE_TYPE = 'N' (un-matched update features)
arcpy.MakeFeatureLayer_management(dfcOutput, "sel_N_layer", "CHANGE_TYPE = 'N'")

# Get mid-points of the selected features; the mid-points carry all the attributes.
arcpy.FeatureVerticesToPoints_management("sel_N_layer", "in_memory\midPts", "MID")

# Find nearest base features from the mid-points
arcpy.Near_analysis("in_memory\midPts", baseFeatures, "300 Feet")

# ====================================================================================
# Note 2:  At this point you can manually inspect the midPts by the NEAR_DIST values; 
#          the lower the values, the higher chance (not always) a match was missed in the 
#          dfc process. Delete features from midPts that have found matching base features 
#          before further process.
# ====================================================================================

# Transfer CHANGE_TYPE values from features of midPts to update features
arcpy.JoinField_management(updateFeatures, "OBJECTID", "in_memory\midPts", "UPDATE_FID", "CHANGE_TYPE")

# Get the count of new roads and the total length; the remaining roads have
# Null values for CHANGE_TYPE.
arcpy.Frequency_analysis(updateFeatures, statsTable, "CHANGE_TYPE", "Shape_Length")