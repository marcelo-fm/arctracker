# PointsSolarRadiation_Example02.py
# Description: For all point locations, calculates total global, direct,
#    diffuse and direct duration solar radiation for a whole year.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
inPntFC = "observers.shp"
outFeatures = "c:/sapyexamples/output/outglobal1.shp"
latitude = 35.75
skySize = 200
timeConfig = TimeMultipleDays(2009, 91, 212)
dayInterval = 14
hourInterval = 0.5
zFactor = 0.3048
calcDirections = 32
zenithDivisions = 8
azimuthDivisions = 8
diffuseProp = 0.3
transmittivity = 0.5
outDirectRad = "C:/sapyexamples/output/outdirectrad1.shp"
outDiffuseRad = "C:/sapyexamples/output/outdiffuserad1.shp"
outDirectDur = "C:/sapyexamples/output/outduration1.shp"

# Execute PointsSolarRadiation...
PointsSolarRadiation(inRaster, inPntFC, outFeatures, "", latitude, skySize, 
                     timeConfig, dayInterval, hourInterval, "INTERVAL", 
                     zFactor, "FROM_DEM", calcDirections, zenithDivisions, 
                     azimuthDivisions,"STANDARD_OVERCAST_SKY", diffuseProp, 
                     transmittivity, outDirectRad, outDiffuseRad, outDirectDur)