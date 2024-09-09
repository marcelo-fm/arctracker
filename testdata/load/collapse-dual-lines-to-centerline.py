# Name: CollapseDualLinesToCenterline_Example2.py
# Description: Create road centerlines and find buildings within a given distance
 
# Import system modules
import arcpy
from arcpy import env
import arcpy.cartography as CA
import arcpy.management as DM
import arcpy.analysis as AN
 
# Set environment settings
env.workspace = "C:/data/Portland.gdb"
 
# Set local variables
inRoadCasingsFeatures = "road_casings"
inHouseFeatures = "houses"

centerlineFeatures = "C:/data/PortlandOutput.gdb/road_centerlines"
bufferFeatures = "C:/data/PortlandOutput.gdb/road_buffers"

# Create centerlines for road casings.
CA.CollapseDualLinesToCenterline(inRoadCasingsFeatures, centerlineFeatures, 80)
 
# Create buffers 100 units from around centerlines.
AN.Buffer(centerlineFeatures, bufferFeatures, 100)

# Select houses by buffers.
DM.SelectLayerByLocation(inHouseFeatures, "intersect", bufferFeatures, 100)