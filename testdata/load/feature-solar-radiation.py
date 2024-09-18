# Name: FeatureSolarRadiation_standalone.py
# Description: Calculate the solar insolation for the whole year 2023 at one week 
#               intervals for engineered features represented by point features.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy.sa import *

# Set environment settings
arcpy.env.workspace = "C:/sapyexamples/solardata.gdb"
arcpy.env.scratchWorkspace = "C:/sapyexamples/outfile.gdb"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Run FeatureSolarRadiation
arcpy.sa.FeatureSolarRadiation(
    in_surface_raster="dem30m.tif",
    in_features="solar_pnts",
    unique_id_field="pntID",
    out_table=r"SolarPnts_radiation_092023",
    start_date_time="1/1/2023",
    end_date_time="12/31/2023",
    time_zone="Mountain_Standard_Time",
    adjust_DST="ADJUSTED_FOR_DST",
    use_time_interval="NO_INTERVAL",
    interval_unit="WEEK",
    interval=1,
    feature_offset=2.5,
    feature_area="Area_FLD",
    feature_slope="Slope_FLD",
    feature_aspect="Aspect_FLD",
    neighborhood_distance="",
    use_adaptive_neighborhood="",
    diffuse_model_type="UNIFORM_SKY",
    diffuse_proportion=0.3,
    transmittivity=0.5,
    analysis_target_device="GPU_THEN_CPU",
    out_join_layer=None
)