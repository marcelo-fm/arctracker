# Name: RasterToASCII_Ex_02.py
# Description: Converts a raster dataset to an ASCII file representing 
#    raster data. 
# Requirements: None

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
outASCII = "c:/output/elevation.asc"

# Run RasterToASCII
arcpy.conversion.RasterToASCII(inRaster, outASCII)