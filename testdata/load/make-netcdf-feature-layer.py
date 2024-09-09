# MakeNetCDFFeatureLayer_Ex_02.py
# Description: Create a feature layer from a netCDF file.
# Requirements: None

# Import system modules
import arcpy

# Set local variables
inNetCDFFile = "C:/data/netcdf/rainfall.nc"
inVariables = "pptx"
inXVariable = "longitude"
inYVariable = "latitude"
outFeatureLayer = "rainfall"
rowDimensions = "station"
ZVariable = ""
MVariable = ""
dimensionValues = ""
valueSelectionMethod = ""

#Execute MakeNetCDFFeatureLayer
arcpy.MakeNetCDFFeatureLayer_md(inNetCDFFile, inVariables, inXVariable, 
                                inYVariable, outFeatureLayer, rowDimensions, 
                                ZVariable, MVariable, dimensionValues, 
                                valueSelectionMethod)