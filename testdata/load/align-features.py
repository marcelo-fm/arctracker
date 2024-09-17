import arcpy
import os

# All input data is in country.gdb and output will also go to this gdb
arcpy.env.workspace = os.path.join(os.getcwd(), "country.gdb")

in_features_orig = "common_border"
in_features_copy = "common_border1"

# Make a copy of the original data 
arcpy.management.CopyFeatures(in_features_orig, in_features_copy)

# Features to which input will be aligned
target_features = "country1_border"
search_dist = "100 Meters"
match_fields = [["A_field", "B_field"]]

arcpy.edit.AlignFeatures(in_features_copy, target_features, search_dist, match_fields)