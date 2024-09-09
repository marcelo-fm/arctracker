# Name: AlignMarkerToStrokeOrFill_standalone_script.py
# Description: Aligns the marker symbol layers of a point feature class to the 
#              nearest stroke or fill symbol layers in a line or polygon 
#              feature class within a specified search distance

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"
arcpy.env.referenceScale = "50000"

# Set local variables
in_point_features = "buildings_points.lyrx"
in_line_or_polygon_features = "roads.lyrx"
search_distance = "2 Points"
marker_orientation = "PERPENDICULAR"

# Execute Align Marker To Stroke Or Fill
arcpy.AlignMarkerToStrokeOrFill_cartography(in_point_features, 
                                            in_line_or_polygon_features, 
                                            search_distance, 
                                            marker_orientation)