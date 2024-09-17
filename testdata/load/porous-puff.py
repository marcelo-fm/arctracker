# Name: PorousPuff_Ex_02.py
# Description: Calculates the time-dependent, two-dimensional 
#              concentration distribution in mass per volume of a 
#              solute introduced instantaneously and at a discrete 
#              point into a vertically mixed aquifer.

# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inTrackFile = "trackfile.txt"
inPorosityRaster = "gwporo"
inThicknessRaster = "gwthick"
mass = 50
dispersionTime = 10000
longitudinalDispersivity = ""
dispersivityRatio = 3 
retardationFactor = "" 
decayCoefficient = 0


# Execute PorousPuff
outPorousPuff = PorousPuff(inTrackFile, inPorosityRaster, inThicknessRaster, 
                        mass, dispersionTime, longitudinalDispersivity,
                        dispersivityRatio, retardationFactor, 
                        decayCoefficient)

# Save the output 
outPorousPuff.save("c:/sapyexamples/output/outporpuff")