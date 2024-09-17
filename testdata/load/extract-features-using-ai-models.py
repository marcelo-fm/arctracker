# Name: ExtractFeaturesUsingAIModels.py
# Description: Extract features using pretrained deep learning models on imagery data.
  
# Import system modules
import arcpy

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set local variables
datapath = "path_to_training_data" 
out_gdb = "path_to_gdb"
predictions = "output_prefix"

# Run Extract Features Using AI Models
arcpy.geoai.ExtractFeaturesUsingAIModels(
    in_raster=datapath,
    mode="Infer and Postprocess", 
    out_location=out_gdb, 
    out_prefix=predictions, 
    pretrained_models="'Building Footprint Extraction - USA'", 
    save_intermediate_output="TRUE", 
    buffer_distance="15 Meters", 
    extend_length="25 Meters", 
    smoothing_tolerance="30 Meters", 
    dangle_length="5 Meters",
    regularization_method="Right Angles",
    poly_tolerance="1 Meters",
    prompt="Bounding Box")