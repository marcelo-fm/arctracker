# Name: BandCollectionStats_Ex_02.py
# Description: Calculates the statistics for a set of raster bands.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRasterBand1 = "sb/sbc1"
inRasterBand2 = "sb/sbc2"
outStatFile = "C:/sapyexamples/output/bandstatfile.txt"

# Execute BandCollectionStats
BandCollectionStats([inRasterBand1, inRasterBand2], outStatFile, "DETAILED")