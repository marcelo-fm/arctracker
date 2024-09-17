# Name: CreateSignatures_Ex_02.py
# Description: Creates an ASCII signature file of classes defined by input 
#    sample data and a set of raster bands.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "sb"
inSamples = "sbtrain"
outSig = "c:/sapyexamples/output/rbsig02.gsg"
sampField = ""

# Execute CreateSignatures
CreateSignatures(inRaster, inSamples, outSig, "COVARIANCE", sampField)