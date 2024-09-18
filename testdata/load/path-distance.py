# Name: PathDistance_Ex_02.py
# Description: Calculates, for each cell, the least accumulative 
#              cost distance to the nearest source, while accounting 
#              for surface distance and horizontal and vertical 
#              cost factors.  
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSource = "observers.shp"
inCostRast = "costraster"
inElev = "elevation"

# The horizontal factor
inHoriz = "backlink2"
# Create the HfForward Object
zeroFactor = 0.5
sideValue = 1.0
myHorizFactor = HfForward(zeroFactor, sideValue)

#The vertical factor
inVertical = "focalcost.tif"
# Create the VfBinary Object
zeroFactor = 1.0
lowCutAngle = -30
highCutAngle = 30
myVerticalFactor = VfBinary(zeroFactor, lowCutAngle, highCutAngle)

maxDist = 50000
optBacklinkOut = "c:/sapyexamples/output/pathbacklink"

# Execute PathDistance
outPathDist = PathDistance(inSource, inCostRast, inElev, inHoriz, 
                           myHorizFactor, inVertical, myVerticalFactor, 
                           maxDist, optBacklinkOut)

# Save the output 
outPathDist.save("c:/sapyexamples/output/pathdistout02")