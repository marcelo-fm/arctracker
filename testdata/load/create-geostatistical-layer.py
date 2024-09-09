# Name: CreateGeostatisticalLayer_Example_02.py
# Description: Uses an existing geostatistical layer to create a new layer,
#              which includes a new feature dataset or variable.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inLayer = "C:/gapyexamples/data/kriging.lyr"
inData = "ca_ozone_pts.shp X=Shape Y=Shape F1=OZONE"
outLayer = "outCGL"

# Execute CreateGeostatisticalLayer
arcpy.GACreateGeostatisticalLayer_ga(inLayer, inData, outLayer)