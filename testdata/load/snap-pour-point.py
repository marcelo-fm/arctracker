# Name: SnapPourPoints_Ex_02.py
# Description: Snaps pour points to the cell of highest 
#              flow accumulation within a specified distance.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPourPoint = "pourpoint"
inFlowAccum = "flowaccumulation.img"
tolerance = 5
pourField = "VALUE"

# Execute SnapPourPoints
outSnapPour = SnapPourPoint(inPourPoint, inFlowAccum, tolerance, 
                            pourField) 

# Save the output 
outSnapPour.save("c:/sapyexamples/output/outsnpprpnt02")