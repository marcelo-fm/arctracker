import arcpy

arcpy.env.workspace = "C:/data"
arcpy.analysis.Clip("majorrds.shp", "study_quads.shp", 
                    "C:/output/studyarea.shp")

arcpy.analysis.Clip("campus.slpk", "building_footprint.shp", 
                    "C:/output/AreaOfInterest.slpk")


# Set local variables
in_features = "majorrds.shp"
clip_features = "study_quads.shp"
out_feature_class = "C:/output/studyarea.shp"

# Run Clip
arcpy.analysis.Clip(in_features, clip_features, out_feature_class)

# Set local variables
scene_service = "https://tiles.arcgis.com/tiles/z2tnIkrLQ2BRzr6P/arcgis/rest/services/2021_02_04_Frankfurt/SceneServer"
mesh_layer_name = "mesh_layer"
clip_features = "AOI.shp"
out_feature_class = "C:/output/studyarea.shp"

# Create a layer of a scene service
mesh_layer = arcpy.management.MakeSceneLayer(scene_service,
                                             mesh_layer_name)

# Run Clip
arcpy.analysis.Clip(mesh_layer, clip_features, out_feature_class)
