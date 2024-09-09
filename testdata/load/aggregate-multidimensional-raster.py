# Name: AggregateMultidimensionalRaster_Ex_02.py
# Description: Aggregates daily precipitation and temperature data into
#           monthly data with the maximum precipitation and temperature values
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

""""
Usage: out_multidimensional_raster = AggregateMultidimensionalRaster(in_multidimensional_raster, dimension,
                                    {aggregation_method}, {variables}, 
                                    {aggregation_def}, {interval_keyword}, {ignore_nodata})
"""

# Define input parameters
inputFile = "C:/sapyexamples/data/dailyclimateData.crf"
dimensionName = "StdTime"
aggregationMethod = "Maximum"
variables = "temperature;precipitation"
aggregationDefinition = "INTERVAL_KEYWORD"
keyword = "MONTHLY"
ignore_nodata = "DATA"

# Execute AggregateMultidimensionalRaster
outAggMultidim = AggregateMultidimensionalRaster(inputFile, dimensionName,
	aggregationMethod, variables, aggregationDefinition, keyword, "", "", "", "",
	ignore_nodata)

# Save the output
outAggMultidim.save("C:/sapyexamples/output/monthlymaxtemp.crf")