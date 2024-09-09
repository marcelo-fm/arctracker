# Name: Select_Example2.py
# Description: Select roads of Class 4 from major roads in the gnatcatcher habitat study area

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/data"

# Set local variables
in_features = "majorrds.shp"
out_feature_class = "C:/output/majorrdsClass4.shp"
where_clause = '"CLASS" = \'4\''

# Run Select
arcpy.analysis.Select(in_features, out_feature_class, where_clause)