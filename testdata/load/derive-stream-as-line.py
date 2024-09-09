# Name: DeriveStreamAsLine_standalone.py
# Description: Generates stream lines from an input surface raster without prior sink filling. 
#              The streams start from locations where the accumulated flow is collected from an area 
#              larger or equal to 2 Hectares considering depressions (polygons).
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
env.workspace = "C:/sapyexamples/data"

# Set the local variables
in_surface_raster = "surface.tif"
in_depressions_data = "depressions.shp"
in_weight_raster = ""
out_streams = "C:/sapyexamples/output/streams.shp"
area_threshold = "2 Hectares"
stream_designation_method = "CONSTANT"

# Execute
DeriveStreamAsLine(in_surface_raster, out_streams, in_depressions_data, 
                   in_weight_raster, area_threshold, stream_designation_method)