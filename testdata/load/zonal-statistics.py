# Name: ZonalStatistics_Ex_standalone.py
# Description: Summarizes values of a multidimensional raster within the zones 
#              of another dataset.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set the analysis environments
arcpy.env.workspace = "C:/sapyexamples/data"

# Set the local variables
inZoneData = "zones.shp"
zoneField = "sampleID"
inValueRaster = "multidimensional_valueraster.crf" 

# Execute ZonalStatistics
outZonalStatistics = ZonalStatistics(inZoneData, zoneField, inValueRaster,
                                     "MAXIMUM", "NODATA", "ALL_SLICES")

# Save the output 
outZonalStatistics.save("C:/sapyexamples/output/zonestatout2.crf")