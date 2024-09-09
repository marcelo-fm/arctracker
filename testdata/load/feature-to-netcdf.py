# FeatureToNetCDF_Ex_02.py
# Description: Converts a feature class to a netCDF file.
# Requirements: None

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data/netcdfgisdata"

# Set local variables
inFeatures = "spotelev.shp"
fieldToVariable = [["Shape.Y", "lat", "degree_north"],
                   ["elevation", "elevation", "meter"]]
outNetCDFFile = "c:/output/pointelev02.nc"
fieldToDimension = "id"

# Execute FeatureToNetCDF
arcpy.FeatureToNetCDF_md(inFeatures, fieldToVariable, outNetCDFFile, 
                         fieldToDimension)