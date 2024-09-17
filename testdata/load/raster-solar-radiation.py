# Name: RasterSolarRadiation_standalone.py
# Description: Calculate solar insolation for the year 2023 at one month 
#  time intervals. Return all output radiation rasters.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy.sa import *

# Set environment settings
arcpy.env.workspace = "C:/sapyexamples/data"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Run RasterSolarRadiation
out_solar_radiation_raster = arcpy.sa.RasterSolarRadiation(
	in_surface_raster="dsm30m_CA.tif",
	start_date_time="1/1/2023",
	end_date_time="12/31/2023",
	in_analysis_mask=None,
	in_slope_raster=None,
	in_aspect_raster=None,
	out_direct_radiation_raster=r"C:\sapyexamples\output\dsm30_direct_radiation_2023_1mo.crf",
	out_diffuse_radiation_raster=r"C:\sapyexamples\output\dsm30_diffuse_radiation_2023_1mo.crf",
	out_duration_raster=r"C:\sapyexamples\output\dsm30_duration_radiation_2023_1mo.crf",
	time_zone="Pacific_Standard_Time",
	adjust_DST="ADJUSTED_FOR_DST",
	use_time_interval="INTERVAL",
	interval_unit="MONTH",
	interval="1",
	neighborhood_distance="",
	use_adaptive_neighborhood="",
	diffuse_model_type="UNIFORM_SKY",
	diffuse_proportion=0.3,
	transmittivity=0.5,
	analysis_target_device="GPU_THEN_CPU"
)

# Save the output 
out_solar_radiation_raster.save(r"C:\sapyexamples\output\dsm30_total_radiation_2023_1mo.crf")