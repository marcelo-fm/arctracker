# Name: FloatToRaster_Ex_02.py
# Description: Converts a file of binary floating-point values representing 
#    raster data to a raster dataset.

# Import system modules
import arcpy

# Set local variables
inASCII = "c:/data/elevation.flt"
outRaster = "c:/output/elev02"

# Run FloatToRaster
arcpy.conversion.FloatToRaster("c:/data/elevation.flt", "c:/output/elev02")