# Name: SimplifySharedEdges_standalone_script.py
# Description: Simplifies input features while maintaining topological 
#              relationships along shared edges. For features included as 
#              shared_edge_features (4th argument of 
#              SimplifySharedEdges_cartography()) only the edges that are shared 
#              with in_features (1st argument) are simplified. 

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/LandUse.gdb"

# Set local variables
in_features = "Water;Parks"
algorithm = "POINT_REMOVE"
tolerance = "10 Meters"
shared_edge_features = "Commercial;Highways;Buildings"
minimum_area = "0 SquareMeters"
barriers = None

# Execute Simplify Shared Edges
arcpy.cartography.SimplifySharedEdges(in_features, algorithm, tolerance, 
                                      shared_edge_features, minimum_area, 
                                      barriers)