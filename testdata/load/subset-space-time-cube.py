# Use the Subset Space Time Cube tool to subset a space-time cube by time 
# and space.

# Import system modules
import arcpy
import os

# Set workspace
arcpy.env.workspace = r"C:\Analysis"
gdb = os.path.join(arcpy.env.workspace, "continents.gdb")
arcpy.env.overwriteOutput = True

# Temporally subset a space-time cube
temperature_stc = "Temperature_STC.nc"
temporal_subset_stc = "Temperature_STC_temporal_subset.nc"

arcpy.stpm.SubsetSpaceTimeCube(temperature_stc, temporal_subset_stc, "NONE", 
                               "USER_DEFINED", None, "", "DEFAULT", None, 
                               "1/1/2012 1/1/2022")

# Spatially subset the data for every continent in the space-time cube
continents = ["Africa", "North_America", "Antarctica", "South_America", "Asia", 
              "Europe", "Australia"]
for continent in continents:
    feature = os.path.join(gdb, c)
    arcpy.stpm.SubsetSpaceTimeCube(temporal_subset_stc, 
                                   continent + "_temperature_subset.nc", 
                                   "FEATURES", "NONE", feature, "INTERSECT")