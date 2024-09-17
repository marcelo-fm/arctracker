# Name: ClassProbability_Ex_02.py
# Description: Creates probability layers for each class in a signature file.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "redl123"
inSigFile = "c:/sapyexamples/data/wedit5.gsg"
maxValue = 100
aPrioriWeight = "EQUAL"
aPrioriFile = ""

# Execute ClassProbability
outClassProbability = ClassProbability(inRaster,inSigFile,
                    maxValue, aPrioriWeight, aPrioriFile)

# Save the output 
outClassProbability.save("c:/sapyexamples/output/classprob01")