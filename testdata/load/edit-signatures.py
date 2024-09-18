# Name: EditSignatures_Ex_02.py
# Description: Edits and updates a signature file by merging, renumbering, 
#    and deleting class signatures.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "redl123"
oldSig = "c:/sapyexamples/data/zsamp12.gsg"
sigRemap = "c:/sapyexamples/data/zsamp7.rmp"
outNewSig = "c:/sapyexamples/output/redlsig.gsg"
interval = ""

# Execute EditSignatures
EditSignatures(inRaster, oldSig, sigRemap, outNewSig, interval)