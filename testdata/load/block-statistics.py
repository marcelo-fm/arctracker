# Name: BlockStatistics_Ex_02.py
# Description: Calculates statistics for a nonoverlapping 
#              neighborhood.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "block"
nbr = NbrAnnulus(1, 3, "MAP")

# Execute BlockStatistics
outBlockStat = BlockStatistics(inRaster, nbr, "MINIMUM", "NODATA")

# Save the output 
outBlockStat.save("C:/sapyexamples/output/blockstat")