# Name: PathBackLink_Ex_02.py
# Description: Defines the neighbor that is the next cell on the least 
#              accumulative cost path to the nearest source, while 
#              accounting for surface distance and horizontal and 
#              vertical cost factors.  
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSource = "source.shp"
inCostRast = "costraster"
inSurfRast = "elevation"

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

inMaxDist = 30000
optOutDist = "c:/sapyexamples/output/pthdstout"

# Execute PathBackLink
outPathBL = PathBackLink(inSource, inCostRast, inSurfRast, 
                         inHoriz, myHorizFactor, inVertical,
                         myVerticalFactor, inMaxDist, optOutDist)

# Save the output 
outPathBL.save("c:/sapyexamples/output/pathblink02")