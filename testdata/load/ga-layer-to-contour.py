# Name: GALayerToContour_Example_02.py
# Description: Exports a geostatistical layer to filled contours with
#              class breaks at 100, 500 and 2000.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
in_geostat_layer = "kriging.lyr"
contour_type = "Filled_contour"
out_feature_class = "C:/gapyexamples/output/krig_filled_contour.shp"
contour_quality = "Presentation"
classification_type = "Manual"
classes_count = ""
classes_breaks = [100, 500, 2000]

# Execute GALayerToContour
arcpy.GALayerToContour_ga(in_geostat_layer, contour_type, out_feature_class,
                          contour_quality, classification_type, classes_count,
                          classes_breaks)