# Create a Spatial Weights Matrix based on Network Data 

# Import system modules
import arcpy

# Set property to overwrite existing output
arcpy.env.overwriteOutput = True

# Local variables...
workspace = r"C:\Data\USCounties\US"

# Set the current workspace (to avoid having to specify the full path to the 
# feature classes each time)
arcpy.env.workspace = workspace

# Create Spatial Weights Matrix 
# Process: Generate Spatial Weights Matrix... 
swm = arcpy.stats.GenerateSpatialWeightsMatrix("USCounties.shp", "MYID",
                                               "euclidean6Neighs.swm",
                                               "K_NEAREST_NEIGHBORS",
                                               "#", "#", "#", 6) 

# Dump Spatial Weights to Database Table
# Process: Convert Spatial Weights Matrix to Table...       
dbf = arcpy.stats.ConvertSpatialWeightsMatrixtoTable("euclidean6Neighs.swm",
                                                     "euclidean6Neighs.dbf")

# Now you can edit the spatial weights (add, subtract and alter
# neighbors and weights)

# Read weights from table back into Spatial Weights Matrix format
# Process: Generate Spatial Weights Matrix... 
swm = arcpy.stats.GenerateSpatialWeightsMatrix("USCounties.shp", "MYID",
                                               "euclidean6Neighs.swm",
                                               "CONVERT_TABLE",
                                               "#", "#", "#", "#", "#", "#",
                                               "euclidean6Neighs.dbf")