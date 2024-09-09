# Name: CollapseHydroPolygon_sample2.py
# Description: Select the rivers and collapse features that are
#               below 6 meters wide to produce centerlines.

# Import System Modules
import arcpy
arcpy.env.workspace = r"C:/data/Hydro.gdb"

# Setting Local Variables
in_features = 'WaterPolygons'
out_line_feature_class = 'HydroCenterlinesOut'
merge_adjacent_input_polygons = False # default is True or "MERGE_ADJACENT"
connection_features = 'WaterLines'
collapse_width = "6 Meters"           # default is '0 Meters'
collapse_width_tolerance = 20         # default is 20
minimum_length = "10 Meters"          # default is '0 Meters' 
taper_length_percentage = 50          # default is 50
out_poly_feature_class =  'HydroPolyOut'

# Select only the Rivers
inputLyr = arcpy.MakeFeatureLayer_management(in_features,
                                             "inputLyr",
                                             "FTYPE = 'rivers'")

# Execute Collapse Hydro Polygon
arcpy.cartography.CollapseHydroPolygon(inputLyr,
                                       out_line_feature_class,
                                       merge_adjacent_input_polygons,
                                       connection_features,
                                       collapse_width,
                                       collapse_width_tolerance,
                                       minimum_length,
                                       taper_length_percentage,
                                       out_poly_feature_class)