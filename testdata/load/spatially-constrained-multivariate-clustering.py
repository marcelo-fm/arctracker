# Creating regions of similar schools districts with at least 100,0000 students each
# Import system modules
import arcpy

# Set property to overwrite existing output, by default
arcpy.env.overwriteOutput = True

# Local variables...
workspace = r"E:\working\data.gdb"
arcpy.env.workspace = workspace

# Create clusters of schools with a minimum of 100,000 students
arcpy.stats.SpatiallyConstrainedMultivariateClustering("CA_schools", "CA_Schools_100k_Students", "NumStudent",
                                          "ATTRIBUTE_VALUE", "NumStudent", 100000, None, None,
                                          "CONTIGUITY_EDGES_CORNERS")

# Create a spatial weights matrix using k nearest neighbors 16 to have more control over the search neighborhood
arcpy.stats.GenerateSpatialWeightsMatrix(r"E:\working\data.gdb\CA_schools", "UID",
                                         r"E:\working\schools_knn_16.swm", "K_NEAREST_NEIGHBORS", "EUCLIDEAN", 1,
                                         None, 16, "NO_STANDARDIZATION", None, None, None, None, "DO_NOT_USE_Z_VALUES")

# Create clusters again this time using the SWM file for search neighborhood and a maximum number
# of students per cluster
arcpy.stats.SpatiallyConstrainedMultivariateClustering("CA_schools", "CA_Schools_SWM_Knn16", "NumStudent", "ATTRIBUTE_VALUE",
                                          "NumStudent", None, 250000, None, "GET_SPATIAL_WEIGHTS_FROM_FILE",
                                          r"E:\working\schools_knn_16.swm")

# Use Summary Statistics with Cluster ID as a case field to see how many students were assigned to each cluster
arcpy.analysis.Statistics("CA_Schools_SWM_Knn16", "School_SummaryStatistics", "NumStudent SUM", "CLUSTER_ID")