# Name: MakeOPeNDAPRasterLayer_Ex_02.py
# Description: Create an OPeNDAP raster layer from a netCDF file.
# Requirements: None

# Import system modules
import arcpy


# Set local variables
in_opendap_URL = "http://cida.usgs.gov/thredds/dodsC/new_gmo"
variable = "pr"
XDimension = "longitude"
YDimension = "latitude"
outRasterLayer = "pr_Layer"
extent = "-124.6875 25.1875 -67.0625 52.8125"
dimensionValues = "time '01/01/1949 12:00:00 AM' '12/31/2010 12:00:00 AM'"
valueSelectionMethod = "BY_VALUE"
cellRegistration = ""

# Execute MakeNetCDFRasterLayer
arcpy.md.MakeOPeNDAPRasterLayer(in_opendap_URL, variable, XDimension, YDimension,
                               outRasterLayer, extent, dimensionValues, 
                               valueSelectionMethod, cellRegistration)