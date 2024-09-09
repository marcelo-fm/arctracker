# Name: StorageCapacity_Standalone.py
# Description: 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy.sa import *

# Set the analysis environments
arcpy.CheckOutExtension("Spatial")
arcpy.env.workspace = "C:/arcpyExamples/data"

# Set local variables
in_surface_raster = "in_surface.tif"
out_table = "fgdb.gdb\out_table"
in_zones = "fgdb.gdb\in_zones"
zone_field = "zone_id"

# Execute StorageCapacity tool
arcpy.sa.StorageCapacity(in_surface_raster, out_table, in_zones, zone_field)