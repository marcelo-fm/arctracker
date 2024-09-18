import arcpy

arcpy.conversion.GPXtoFeatures('c:\\GPX_Files\\Hike.gpx', 'c:\\gisData\\Hike.shp', 'POINTS')