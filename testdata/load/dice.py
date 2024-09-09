# Dice.py
# Description: Simple example showing use of Dice tool

 
# Import system modules
import arcpy
from arcpy import env
env.workspace = "C:/data/gdb/canada.gdb"

# Set variables
fcName = "coastline"
outFcName = "coastline_Dice_750k"
vertLimit = 750000

#Process: Use the Dice function
arcpy.Dice_management (fcName, outFcName, vertLimit)