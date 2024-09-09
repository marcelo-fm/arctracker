# Name: TableToNetCDF_Ex_02.py
# Description: 
# Requirements: none

# Import system modules
import arcpy

# Set local variables
inTable = "c:/data/netcdfgisdata/rainfall.dbf"
fieldVariableUnits = "longitude longitude degree_east;latitude latitude degree_north"
outNetCDFFile = "c:/output/rain.nc"
fieldDimensionUnits = "station station"

# Execute SelectByDimension
import arcpy
arcpy.TableToNetCDF_md(inTable, fieldVariableUnits, outNetCDFFile, fieldDimensionUnits)