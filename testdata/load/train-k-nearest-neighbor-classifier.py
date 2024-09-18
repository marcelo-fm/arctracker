# Import system modules 
import arcpy 
from arcpy.ia import * 
 
# Check out the ArcGIS Image Analyst extension license 
arcpy.CheckOutExtension("ImageAnalyst") 
 
# Define input parameters 
in_raster = r"C:/Data/ landsat.tif" 
in_training_features = r"C:/Data/training_sample.shp" 
out_classifier_definition = r"C:/Data/trained_knn.ecd" 
number_of_neighbors = 5
attributes = "COLOR;MEAN;STD;COUNT;COMPACTNESS;RECTANGULARITY"
     
# Execute  - train K-Nearest Neighbor Classifier
arcpy.ia.TrainKNearestNeighborClassifier(in_raster, in_training_features, out_classifier_definition,  
           number_of_neighbors, attributes)