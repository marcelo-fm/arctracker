# Name: AnalyzeDatasets.py
# Description: analyzes all datasets in an enterprise geodatabase
#              for a given user.

# Import system modules
import arcpy
import os

# set workspace
# the user in this workspace must be the owner of the data to analyze.
workspace = "C:\\MyProject\\MyDataConnection.sde"

# set the workspace environment
arcpy.env.workspace = workspace

# NOTE: Analyze Datasets can accept a Python list of datasets.

# Get the user name for the workspace
userName = arcpy.Describe(workspace).connectionProperties.user

# Get a list of all the datasets the user owns by using a wildcard that incldues the user name
# First, get all the stand alone tables, feature classes and rasters.
dataList = arcpy.ListTables(userName + "*") + arcpy.ListFeatureClasses(userName + "*") + arcpy.ListRasters(userName + "*")

# Next, for feature datasets get all of the datasets and featureclasses
# from the list and add them to the master list.
for dataset in arcpy.ListDatasets(userName + "*", "Feature"):
    arcpy.env.workspace = os.path.join(workspace,dataset)
    dataList += arcpy.ListFeatureClasses(userName + "*") + arcpy.ListDatasets(userName + "*")

# reset the workspace
arcpy.env.workspace = workspace

# Execute analyze datasets
# Note: to use the "SYSTEM" option the workspace user must be an administrator.
arcpy.AnalyzeDatasets_management(workspace, "NO_SYSTEM", dataList, "ANALYZE_BASE","ANALYZE_DELTA","ANALYZE_ARCHIVE")
print("Analyze Complete")