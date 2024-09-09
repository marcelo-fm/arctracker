# Name: DimensionalMovingStatistics_standalone.py
# Description: Calculates majority on a multidimensional raster 
#                along its time dimension.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environment
env.workspace = "C:/sapyexamples/data"

# Set local variables
in_raster = "mining_location.crf"
dimension = "StdTime"
backward_window = 2
forward_window = 2
nodata_handling = "FILL_NODATA"
statistics_type = "MAJORITY"

# Execute DimensionalMovingStatistics
out_dimstats = DimensionalMovingStatistics(in_raster, dimension, 
                 backward_window, forward_window, nodata_handling, 
                 statistics_type)

# Save the output
out_dimstats.save("C:/sapyexamples/output/mining_location_out.crf")