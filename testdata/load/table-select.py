# Name: TableSelect_Example2.py
# Description: Select class4 roads from the major roads gnatcatcher habitat study area

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/data"

# Set local variables
in_features = "majorrds.shp"
out_feature_class = "C:/output/majorrdsCl4.shp"
where_clause = '"CLASS" = \'4\''

# Run TableSelect
arcpy.analysis.TableSelect(in_features, out_feature_class, where_clause)