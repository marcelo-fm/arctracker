# Name: DOFToObstacleFeatures_Example2.py
# Description: Convert DOF records to obstacle features.

# Import system modules
import os
import arcpy

# Set local variables
working_mty = r"d:\working\monterey"
in_dof_csv = os.path.join(working_mty, "dof.csv")
out_obx = os.path.join(working_mty, "results.gdb", "obstacles")
out_buf = os.path.join(working_mty, "results.gdb", "buffers")
aoi = os.path.join(working_mty, "tasking.gdb", "mtyAOI")

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(32611) # UTM Zone 11

# Run DOFToObstacleFeatures
arcpy.intelligence.DOFToFeatures(in_dof_csv, out_obx, out_buf, aoi)