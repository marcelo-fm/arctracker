# Name: SmoothSharedEdges_standalone_script.py
# Description: Smoothes input features while maintaining topological 
#              relationships along shared edges. For features included as 
#              shared_edge_features (4th argument of 
#              SmoothSharedEdges_cartography()) only the edges that are shared 
#              with in_features (1st argument) are smoothed. 

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/LandUse.gdb"

# Set local variables
in_features = "Water;Parks"
algorithm = "PAEK"
tolerance = "10 Meters"
shared_edge_features = "Commercial;Highways;Buildings"
barriers = None

# Execute Smooth Shared Edges
arcpy.cartography.SmoothSharedEdges(in_features, algorithm, tolerance, 
                                    shared_edge_features, barriers)