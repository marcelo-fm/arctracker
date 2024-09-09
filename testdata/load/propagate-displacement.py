# Name: PropagateDisplacement_standalone_script.py
# Description: Propagate the displacement of road features to nearby buildings
# Author: ESRI
 
# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
in_features = "footprints.lyr"
displacement_features = "displacement.lyr"
adjustment_style = "AUTO"

# Execute Propagate Displacment
arcpy.PropagateDisplacement_cartography(in_features, displacement_features, adjustment_style)