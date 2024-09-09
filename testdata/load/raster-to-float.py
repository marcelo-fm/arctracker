# Name: RasterToFloat_Ex_02.py
# Description: Converts a raster dataset to a file of binary floating-point
#     values representing raster data.
# Requirements: None

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
outFloat = "c:/output/elevation.flt"

# Run RasterToFloat
arcpy.conversion.RasterToFloat(inRaster, outFloat)