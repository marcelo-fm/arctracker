# Name: RasterToPolyline_Ex_02.py
# Description: Converts a raster dataset to polyline features.
# Requirements: None

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
inRaster = "flowstr"
outLines = "c:/output/flowstream.shp"
backgrVal = "ZERO"
dangleTolerance = 50
field = "VALUE"

# Run RasterToPolygon
arcpy.conversion.RasterToPolyline(inRaster, outLines, backgrVal, 
                                  dangleTolerance, "SIMPLIFY", field)