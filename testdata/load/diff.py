# Name: Diff_Ex_02.py
# Description: Determines which values from the first input are
#              logically different from the values of the second input
#              on a cell-by-cell basis within the Analysis window
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = "degs"
inRaster2 = "negs"

# Execute Diff
outDiff = Diff(inRaster1, inRaster2)

# Save the output 
outDiff.save("C:/sapyexamples/output/outdiff")