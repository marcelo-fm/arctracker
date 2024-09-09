import arcpy
arcpy.env.workspace = 'C:/project_directory'

# Create a feature layer from the 3D Object feature class
feature_class = "city_models.gdb/Downtown_Buildings"
feature_layer = os.path.basename(feature_class)
arcpy.MakeFeatureLayer_management(feature_class, feature_layer)

# Select a subset of features to export
# The default OBJECTID field is used below to process a subset of features
object_ids = '1,5,10'
sql_query = f"OBJECTID IN ({object_ids})"
arcpy.management.SelectLayerByAttribute(feature_layer, "NEW_SELECTION", sql_query)

# Export the selected features to model files on disk
arcpy.management.Export3DObjects(feature_layer, "exported_models", ["FMT3D_GLB"])
arcpy.management.Delete(feature_layer)