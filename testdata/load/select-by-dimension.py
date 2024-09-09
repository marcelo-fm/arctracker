# Name: SelectBydimension_Ex_02.py
# Description: Updates the netCDF layer display based on the dimension value.
# Requirements: none

# Import system modules
import arcpy

# Set local variables
inNetCDFLayer = "rainfall" 
valueSelect01 = ["lat", 20]
valueSelect02 = ["lon", 45]  
dimensionValues = [valueSelect01, valueSelect02]
valueSelectionMethod = ""

# Execute SelectByDimension
arcpy.SelectByDimension_md(inNetCDFLayer, dimensionValues, valueSelectionMethod)