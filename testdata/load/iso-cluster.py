# Name: IsoCluster_Ex_02.py
# Description: Uses an isodata clustering algorithm to determine the 
#    characteristics of the natural groupings of cells in multidimensional 
#    attribute space and stores the results in an output ASCII signature file.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "redlands"
outSig = "redlndiso.gsg"
classes = 5
cycles = 20
minMembers = 50
sampInterval = 15

# Execute IsoCluster
IsoCluster(inRaster, outSig, classes, cycles, minMembers, sampInterval)