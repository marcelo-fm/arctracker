# Name: CellStatistics_Ex_standalone.py
# Description: Calculates a per-cell statistic from multiple multiband rasters
#               and process as multiband.
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

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