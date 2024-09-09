# MakeNetCDFTableView_Ex_02.py
# Description: Create a table view from a netCDF file.
# Requirements: None

#Import system modules
import arcpy

# Set local variables
inNetCDFFile = "c:/data/netcdf/precipmonmean.nc"
variable = "precip;humidity"
outTableView = "precipmonmeantable"
rowDimension = "time"
dimensionValue = ""
valueSelectionMethod = ""

# Execute MakeNetCDFTableView
arcpy.MakeNetCDFTableView_md(inNetCDFFile, variable, outTableView, rowDimension, 
                             dimensionValue,valueSelectionMethod)