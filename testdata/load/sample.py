# Name: Sample_Ex_04.py
# Description: Creates a table that shows, for each polygon, the maximum temperature value within the period [1999-01-01T00:00:00 , 2019-01-01-T00:00:00]
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRasters = "temperature_1990_2019.nc"
locations = "observers_polygons.shp"
outTable = "C:/sapyexamples/output/samptable_04.dbf"
sampMethod = "BILINEAR"
uniqueIDField = "OBSERVATIONID"
process_as_multidimensional = True
# StdTime in acquisition_definition is the name of the dimension in inRasters that are related with time
# 1999-01-01T00:00:00 in acquisition_definition is the start time of the period
# 2019-01-01-T00:00:00 in acquisition_definition is the end time of the period
acquisition_definition = "StdTime 1999-01-01T00:00:00 2019-01-01-T00:00:00"
statistic_method = "MAXIMUM"

# Execute Sample
# for each polygon in locations, the maximum temperature value within the period [1999-01-01T00:00:00 , 2019-01-01-T00:00:00] will be extracted
Sample(inRasters, locations, outTable, sampMethod, uniqueIDField, process_as_multidimensional, acquisition_definition, statistic_method)