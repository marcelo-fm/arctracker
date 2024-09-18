# Name: SplitLineAtPoint_Example.py
# Description: Split line features based on near point features.

import arcpy

arcpy.env.workspace = "C:/data"
inFeatures = "streets.shp"
pointFeatures = "events.shp"
outFeatureclass = "splitline_out.shp"
searchRadius = "20 Meters"

arcpy.management.SplitLineAtPoint(inFeatures, pointFeatures, outFeatureclass, 
                                  searchRadius)