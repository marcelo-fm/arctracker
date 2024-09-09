# Name: ConvertLabelsToGraphics.py
# Description: Find all the maps in the project and
#              convert labels to graphics for each map

# import system modules

import arcpy

# Loop through the project, find all the maps, and
#   convert labels to graphics for each map,
#   using the name of the map as part of the graphics layer suffix 
project = arcpy.mp.ArcGISProject("D:\\data\\myproject.aprx")
for mp in project.listMaps():
    print("Converting labels to graphics for: " + mp.name)
    arcpy.cartography.ConvertLabelsToGraphics(
            mp, 10000, 'ALL_LAYERS', '', 'Graphics_' + mp.name, 'MAXOF', 
            'GRAPHICS_LAYER_PER_FEATURE_LAYER', 'ONLY_PLACED',  
            'GraphicsLayers_' + mp.name)