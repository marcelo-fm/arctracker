# Name: CellStatistics_Ex_standalone.py
# Description: Calculates a per-cell statistic from multiple multiband rasters
#               and process as multiband.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/sapyexamples/data"

# Set the local variables
inRaster01 = "degs_MB"
inRaster02 = "negs_MB"
inRaster03 = "cost_MB"

# Execute CellStatistics
outCellStatistics = CellStatistics([inRaster01, inRaster02, inRaster03], "RANGE", "NODATA", "MULTI_BAND")

# Save the output 
outCellStatistics.save("C:/sapyexamples/output/cellstats_MB.tif")