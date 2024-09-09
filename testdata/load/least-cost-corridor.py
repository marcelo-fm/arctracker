# Name: LeastCostCorridor_Ex_02.py
# Description: Calculates a potential wildlife corridor between two known 
#               protected areas.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set environment settings
env.workspace = "C:/arcpyexamples/data"

# Set local variables
in_accumulative_cost_distance_raster1 = "distaccum_s1.tif"
in_back_direction_raster1 = "backdir_s1.tif"
in_accumulative_cost_distance_raster2 = "distaccum_s2.tif"
in_back_direction_raster2 = "backdir_s2.tif"
threshold_method = "ACCUMULATIVE_COST" 
threshold = 500

# Run Least Cost Corridor
out_LCC_raster = LeastCostCorridor(
    in_accumulative_cost_distance_raster1, in_back_direction_raster1, 
    in_accumulative_cost_distance_raster2, in_back_direction_raster2, 
    "ACCUMULATIVE_COST", "500")

# Save the output 
out_LCC_raster.save("c:/arcpyexamples/output/corridor.tif")