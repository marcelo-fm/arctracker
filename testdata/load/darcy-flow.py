# Name: DarcyFlow_Ex_02.py
# Description: Calculates the groundwater volume balance residual and other
#    outputs for steady flow in an aquifer.
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
outDirectionRaster = "C:/sapyexamples/output/outdarcydir"
outMagnitudeRaster = "C:/sapyexamples/output/outdarcymag"

# Execute DarcyFlow
outDarcyFlow = DarcyFlow(inHeadRaster, inPorosityRaster, inThicknessRaster,
                         inTransmissivityRaster, outDirectionRaster,
                         outMagnitudeRaster)

# Save the output 
outDarcyFlow.save("C:/sapyexamples/output/outdarcyflow")