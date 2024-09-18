# Name: MLClassify_Ex_02.py
# Description: Performs a maximum likelihood classification on a set of 
#    raster bands.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "redlands"
sigFile = "c:/sapyexamples/data/wedit5.gsg"
probThreshold = "0.0"
aPrioriWeight = "EQUAL"
aPrioriFile = ""
outConfidence = "c:/sapyexamples/output/redconfmlc"


# Execute 
mlcOut = MLClassify(inRaster, sigFile, probThreshold, aPrioriWeight, 
                    aPrioriFile, outConfidence) 

# Save the output 
mlcOut.save("c:/sapyexamples/output/redmlc02")