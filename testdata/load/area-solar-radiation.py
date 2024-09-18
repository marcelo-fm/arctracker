# Name: AreaSolarRadiation_example02.py
# Description: Derives incoming solar radiation from a raster surface. 
#              Outputs a global radiation raster and optional direct, diffuse and direct duration rasters
#              for a specified time period. (April to July).
#              
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/output"

# Set local variables
inRaster = "C:/sapyexamples/data/solar_dem"
latitude = 35.75
skySize = 400
timeConfig = TimeMultipleDays(2008, 91, 212)
dayInterval = 14
hourInterval = 0.5
zFactor = 0.3048
calcDirections = 32
zenithDivisions = 16
azimuthDivisions = 16
diffuseProp = 0.7
transmittivity = 0.4
outDirectRad = ""
outDiffuseRad = ""
outDirectDur = Raster("C:/sapyexamples/output/dir_dur")


# Execute AreaSolarRadiation
outGlobalRad = AreaSolarRadiation(inRaster, latitude, skySize, timeConfig,
   dayInterval, hourInterval, "NOINTERVAL", zFactor, "FLAT_SURFACE",
   calcDirections, zenithDivisions, azimuthDivisions, "UNIFORM_SKY",
   diffuseProp, transmittivity, outDirectRad, outDiffuseRad, outDirectDur)

# Save the output 
outGlobalRad.save("C:/sapyexamples/output/glob_rad")