# Name: ASCIIToRaster_Ex_02.py
# Description: Converts an ASCII file representing raster data to a raster 
#    dataset.

# Import system modules
import arcpy

# Set local variables
inASCII = "c:/data/elevation.asc"
outRaster = "c:/output/elevation02"
rasterType = "INTEGER"

# Run ASCIIToRaster
arcpy.conversion.ASCIIToRaster(inASCII, outRaster, rasterType)