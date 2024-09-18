# Name: Dendrogram_Ex_02.py
# Description: Constructs a tree diagram showing attribute distances between
#     sequentially merged classes in a signature file.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy.sa import *

# Set local variables
inSig = "c:/sapyexamples/data/zsamp12.gsg"
outDendro = "c:/sapyexamples/output/z12dend.txt"
lineLength = ""

# Execute Dendrogram
Dendrogram(inSig, outDendro, "VARIANCE", lineLength)