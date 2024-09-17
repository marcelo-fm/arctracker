# Name: Corridor_Ex_02.py
# Description: Calculate a potential wildlife corridor between 
#              two known protected areas.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inCostRaster = "costdist01"
nextCostRaster = "cotdist02"

# Execute Corridor
outCorridor = Corridor(inCostRaster, nextCostRaster) 

#Limit the corridor to a threshold to show a potential corridor
corridor = Con(outCorridor, 1, 0, "VALUE < 100")

# Save the output 
outCorridor.save("C:/sapyexamples/output/costout")