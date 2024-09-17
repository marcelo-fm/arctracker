# Name: GetSceneLayerCount.py
# Description: Gets the number of features from a scene service

# Import system modules
import arcpy

out_layer = 'Hamburg_Buildings'

# Make a layer from a scene service
arcpy.management.MakeSceneLayer('http://scene.arcgis.com/arcgis/rest/services/Hosted/Building_Hamburg/SceneServer/layers/0',
                                out_layer)
print("Created Scene Layer")

# Get the number of features from the scene service
result = arcpy.management.GetCount(out_layer)
print('{} has {} records'.format(out_layer, result[0]))