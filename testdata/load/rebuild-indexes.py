# Name: RebuildIndexes.py
# Description: rebuilds indexes on delta tables for all datasets in an
# enterprise geodatabase

# Import system modules
import arcpy, os

# set workspace
workspace = arcpy.GetParameterAsText(0)

# set the workspace environment
arcpy.env.workspace = workspace

# NOTE: Rebuild indexes can accept a Python list of datasets.

# Get a list of all the datasets the user has access to.
# First, get all the stand alone tables, feature classes and rasters.
dataList = arcpy.ListTables() + arcpy.ListFeatureClasses() + arcpy.ListRasters()

# Next, for feature datasets get all of the datasets and featureclasses
# from the list and add them to the master list.
for dataset in arcpy.ListDatasets("", "Feature"):
    arcpy.env.workspace = os.path.join(workspace,dataset)
    dataList += arcpy.ListFeatureClasses() + arcpy.ListDatasets()

# reset the workspace
arcpy.env.workspace = workspace

# Get the user name for the workspace
userName = arcpy.Describe(workspace).connectionProperties.user.lower()

# remove any datasets that are not owned by the connected user.
userDataList = [ds for ds in dataList if ds.lower().find(".%s." % userName) > -1]

# Execute rebuild indexes
# Note: to use the "SYSTEM" option the workspace user must be an administrator.
arcpy.RebuildIndexes_management(workspace, "NO_SYSTEM", userDataList, "ALL")
print('Rebuild Complete')