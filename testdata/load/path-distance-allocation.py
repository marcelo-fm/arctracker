# Name: PathAllocation_Ex_02.py
# Description: Calculates, for each cell, its nearest source based 
#              on the least accumulative cost over a cost surface, 
#              while accounting for surface distance and horizontal 
#              and vertical cost factors. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSource = "observers.shp"
costRast = "costraster"
surfaceRast = "elevation"

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

maxDist = 25000
valRaster = "eucdirout"
sourceField = "FID"
optPathDistOut = "c:/sapyexamples/output/optdistpath"
optPathBLOut = "c:/sapyexamples/output/pathblinkout"

# Execute PathAllocation
pathAlloc = PathAllocation(inSource, costRast, surfaceRast, 
                           inHoriz, myHorizFactor, inVertical, myVerticalFactor, 
                           maxDist, valRaster, sourceField, 
                           optPathDistOut, optPathBLOut)

# Save the output 
pathAlloc.save("c:/sapyexamples/output/allocpath02")