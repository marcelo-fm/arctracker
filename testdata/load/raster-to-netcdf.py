# RasterToNetCDF_Ex_02.py
# Description: Converts a raster dataset to a netCDF file.
# Requirements: None

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "C:/data/elevation"
outNetCDFFile = "C:/output/elevnetcdf.nc"
variable = "elevation"
units = "meter"
XDimension = "x"
YDimension = "y"
bandDimension = ""
compressionLevel = ""

# Process: RasterToNetCDF
arcpy.md.RasterToNetCDF(inRaster, outNetCDFFile, variable, units, 
                        XDimension, YDimension, bandDimension, compressionLevel)