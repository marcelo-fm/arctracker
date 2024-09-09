# Name: ResolveRoadConflicts_standalone_script.py
# Description: Resolves symbology conflicts between roads by separating them apart from each other
# Author: ESRI
 
# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"
env.referenceScale = "50000"

# Set local variables
in_layers = "C:/data/roads.lyr;C:/data/streets.lyr;C:/data/highways.lyr"
hierarchy_field = "hierarchy"
out_displacement_features = "C:/data/cartography.gdb/transportation/displace"

# Execute Resolve Road Conflicts
arcpy.ResolveRoadConflicts_cartography(in_layers, level_field, out_displacement_features)