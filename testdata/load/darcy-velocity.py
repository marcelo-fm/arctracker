# Name: DarcyVelocity_Ex_02.py
# Description: Calculates the groundwater seepage velocity 
#              vector (direction and magnitude) for steady 
#              flow in an aquifer.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inHeadRaster = "gwhead"
inPorosityRaster = "gwporo"
inThicknessRaster = "gwthick"
inTransmissivityRaster = "gwtrans"
outMagnitudeRaster = "C:/sapyexamples/output/outdarcymag"

# Execute DarcyVelocity
outDarcyVelocity = DarcyVelocity(inHeadRaster, inPorosityRaster, inThicknessRaster,
                            inTransmissivityRaster, outMagnitudeRaster)

# Save the output 
outDarcyVelocity.save("C:/sapyexamples/output/outdarcyvel")