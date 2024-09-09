# Name: DeriveStreamAsRaster_standalone.py
# Description: Generates a stream raster considering real depressions where 
#              streams start from locations with catchment areas larger than 2 Hectares.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set the local variables
in_surface_raster = "surface.tif"
in_depressions_data = "depressions.tif"
stream_raster = "C:/arcpyExamples/outputs/stream_raster.tif"

# Execute DeriveStreamAsRaster
out_stream_raster = DeriveStreamAsRaster(in_surface_raster, in_depressions_data, 
                                        "", "2 Hectares", "UNIQUE", "")
# Save the output
out_stream_raster.save(stream_raster)