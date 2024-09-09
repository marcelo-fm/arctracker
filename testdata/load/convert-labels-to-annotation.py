# Name: ConvertLabelsToAnnotation.py
# Description: Find all the maps in the project and
#              convert labels to annotation for each map

# import system modules

import arcpy

# Loop through the project, find all the maps, and
#   convert labels to annotation for each map,
#   using the name of the map as part of the annotation suffix 
project = arcpy.mp.ArcGISProject("D:\\data\\myproject.aprx")
for mp in project.listMaps():
    print("Converting labels to annotation for: " + mp.name)
    arcpy.cartography.ConvertLabelsToAnnotation(
            mp, 10000, 'D:/data/Cobourg.gdb', 'Anno_' + mp.name, 'MAXOF', 
            'ONLY_PLACED', 'REQUIRE_ID', 'STANDARD', '', '', 
            'AnnoLayers_' + mp.name, 'ALL_LAYERS', '', 'SINGLE_FEATURE_CLASS', 
            'MERGE_LABEL_CLASS')