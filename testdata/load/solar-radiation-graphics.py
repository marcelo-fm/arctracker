# Name: SolarRadiationGraphics_Ex_02.py
# Description: Derives raster representations of a hemispherical viewshed, 
#    sunmap, and skymap, which are used in the calculation of direct, diffuse, 
#    and global solar radiation.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
pntFC = "observers.shp"
skySize = 200
zOffset = 2
directions = 32
latitude = 52
timeConfig = TimeMultipleDays(2009, 91, 212)
dayInterval = 14
hourInterval = 0.5
outSunMap = "c:/sapyexamples/output/sunmap"
zenDivisions = 8
aziDivisions = 8
outSkyMap = "c:/sapyexamples/output/skymap"

# Execute SolarRadiationGraphics
outViewshedMap = SolarRadiationGraphics(inRaster, pntFC, skySize, zOffset, 
                                    directions, latitude, timeConfig,
                                    dayInterval, hourInterval, outSunMap,
                                    zenDivisions, aziDivisions, outSkyMap)

# Save the output
outViewshedMap.save("c:/sapyexamples/output/viewmap")