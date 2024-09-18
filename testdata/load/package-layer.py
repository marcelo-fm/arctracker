# Import system modules
import os
import arcpy

prj = arcpy.mp.ArcGISProject(r"\\fileServe\projects\Timbuktu\Timbuktu.aprx")
maps = prj.listMaps()[0]
lyrs = maps.listLayers()
for lyr in lyrs:
    if lyr.isFeatureLayer:
        arcpy.management.PackageLayer(lyr, os.path.join("c:/temp", lyr.name + ".lpkx"))