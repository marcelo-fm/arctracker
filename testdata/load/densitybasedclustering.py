# The following stand-alone Python script demonstrates how to use 
# the DensityBasedClustering function with time to find space-time clusters.

# Time field and Search time interval only supported by DBSCAN and OPTICS methods

# Import system modules
import arcpy
import os

# Overwrite existing output, by default
arcpy.env.overwriteOutput = True

# Local variables...
workspace = r"E:\working\data.gdb"
arcpy.env.workspace = workspace

# Run Density-based Clustering with DBSCAN Cluster Method, and choose 50 as the minimum
# features per cluster, 200 meter search distance, and 10 minute search time interval
arcpy.stats.DensityBasedClustering("New_York_Taxi_PickingUp", "New_York_Taxi_DBSCAN_Time", 
                        "DBSCAN",  50, "200 Meters", None, "Pickup_Time", "10 Minutes")

# Run Density-based Clustering with OPTICS Method, and choose 50 as the minimum
# of features per cluster, 200 meter search distance, and 10 minute search time interval. 
# Using 15 as the cluster sensitivity to create a higher number of dense clusters
arcpy.stats.DensityBasedClustering("New_York_Taxi_PickingUp", "New_York_Taxi_OPTICS_Time", 
                        "OPTICS",  50, "200 Meters", 15, "Pickup_Time", "10 Minutes")