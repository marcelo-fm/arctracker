# Name: MakeNetCDFRasterLayer_Ex_02.py
# Description: Create a raster layer from a netCDF file.
# Requirements: None

# Import system modules
import arcpy


# Set local variables
inNetCDFFile = "C:/data/netcdf/rainfall.nc"
variable = "pptx"
XDimension = "lon"
YDimension = "lat"
outRasterLayer = "rainfall"
bandDimmension = ""
dimensionValues = ""
valueSelectionMethod = ""
cellRegistration = ""

# Execute MakeNetCDFRasterLayer
arcpy.md.MakeNetCDFRasterLayer(inNetCDFFile, variable, XDimension, YDimension,
                               outRasterLayer, bandDimmension, dimensionValues, 
                               valueSelectionMethod, cellRegistration)