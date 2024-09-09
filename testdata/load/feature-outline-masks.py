# Name: FeatureOutlineMasks_standalone_script.py
# Description: Creates mask polygons at a specified distance and shape
#           around symbolized features. 
 
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
input_layer = "roads.lyrx"
output_fc = "cartography.gdb/transportation/roads_fom_polys"
reference_scale = "25000"
spatial_reference = arcpy.SpatialReference(4326) 
margin = "5 meters"
method = "EXACT_SIMPLIFIED"
mask_for_non_placed_anno = "ONLY_PLACED"
attributes = "ALL"

# Execute Feature Outline Masks
arcpy.FeatureOutlineMasks_cartography(input_layer,
                                      output_fc,
                                      reference_scale,
                                      spatial_reference,
                                      margin, method,
                                      mask_for_non_placed_anno,
                                      attributes)