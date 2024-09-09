'''****************************************************************************
Name: DecimateTinNodes Example
Description: This script demonstrates how to use the 
             DecimateTinNodes tool.
****************************************************************************'''

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set Local Variables
inTin = "elevation"
method = "COUNT 5000"
copyBrk = "BREAKLINES"
# Ensure output name is unique
outTin = arcpy.CreateUniqueName("simple_elev")

#Execute DecimateTinNodes
arcpy.ddd.DecimateTinNodes(inTin, outTin, method, copyBrk)