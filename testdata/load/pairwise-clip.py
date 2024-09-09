# Description: Clip major roads that fall within the study area. 

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/data"

# Set local variables
in_features = "majorrds.shp"
clip_features = "study_quads.shp"
out_feature_class = "C:/output/studyarea.shp"

# Run Pairwise Clip
arcpy.analysis.PairwiseClip(in_features, clip_features, out_feature_class)