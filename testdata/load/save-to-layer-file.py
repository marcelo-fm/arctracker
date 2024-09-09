# Description: Save a layer to a file on disk

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/data"

# Set local variables
in_features = "study_quads.shp"
where_clause = '"NAME" = \'LA MESA\''
in_layer = "studyquadsLyr"
out_layer_file = "studyquadsLyr.lyrx"

# Run MakeFeatureLayer
arcpy.management.MakeFeatureLayer(in_features, "study_quads_lyr", where_clause)

# Run SaveToLayerFile
arcpy.management.SaveToLayerFile("study_quads_lyr", out_layer_file, "ABSOLUTE")