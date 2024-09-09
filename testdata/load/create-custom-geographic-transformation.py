# Name: CreateCustomGeographicTransformation.py
# Description: Create a custom geographic transformation in the default directory.

# import system modules
import arcpy

# set the variables
geoTransfmName = "cgt_geocentric2"

# create a spatial reference object for GCS_Tokyo
inGCS = arcpy.SpatialReference("Tokyo")

# create a spatial reference object for GCS_WGS_1984
outGCS = arcpy.SpatialReference("WGS 1984")

customGeoTransfm = "GEOGTRAN[METHOD['Geocentric_Translation'],PARAMETER['X_Axis_Translation',''],PARAMETER['Y_Axis_Translation',''],PARAMETER['Z_Axis_Translation','']]"

arcpy.management.CreateCustomGeoTransformation(geoTransfmName, inGCS, outGCS, customGeoTransfm)