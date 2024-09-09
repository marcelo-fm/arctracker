# Name: RasterToPoint_Ex_02.py
# Description: Converts a raster dataset to point features.
# Requirements: None

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
inRaster = "source.img"
outPoint = "c:/output/source.shp"
field = "VALUE"

# Run RasterToPoint
arcpy.conversion.RasterToPoint(inRaster, outPoint, field)