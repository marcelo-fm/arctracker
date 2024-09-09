# Import system modules
import arcpy

# Set property to overwrite existing outputs
arcpy.env.overwriteOutput = True

# Set the work space to a gdb
arcpy.env.workspace = r"C:\Data\Landsat.gdb"

# Using a forest-based model to classify a Landsat image. The TrainingPolygons feature 
# class was created manually and is used to train the model to 
# classify the remainder of the Landsat image.

prediction_type = "PREDICT_RASTER"
in_features = r"TrainingPolygons"
variable_predict = "LandClassName"
treat_variable_as_categorical = "CATEGORICAL" 
explanatory_variables = None
distance_features = None
explanatory_rasters = [["Band1", "false"], ["Band2", "false"], ["Band3", "false"]]
features_to_predict = None
output_features = None
output_raster = r"PredictionSurface"
explanatory_variable_matching = None
explanatory_distance_matching = None
explanatory_rasters_matching = [["Band1", "Band1"], ["Band2", "Band2"], ["Band3", "Band3"]]
output_trained_features = None
output_importance_table = None
use_raster_values = True
number_of_trees = 100
minimum_leaf_size = None
maximum_level = None
sample_size = 100
random_sample = None
percentage_for_training = 10

arcpy.stats.Forest(prediction_type, in_features, variable_predict,
    treat_variable_as_categorical, explanatory_variables, distance_features,
    explanatory_rasters, features_to_predict, output_features, output_raster,
    explanatory_variable_matching, explanatory_distance_matching, 
    explanatory_rasters_matching, output_trained_features, output_importance_table,
    use_raster_values, number_of_trees, minimum_leaf_size, maximum_level,
    sample_size, random_sample, percentage_for_training)