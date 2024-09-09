# Name: RasterToPolygon_Ex_02.py
# Description: Converts a raster dataset to polygon features.
# Requirements: None

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
inRaster = "zone"
outPolygons = "c:/output/zones.shp"
field = "VALUE"

# Run RasterToPolygon
arcpy.conversion.RasterToPolygon(inRaster, outPolygons, "NO_SIMPLIFY", field)