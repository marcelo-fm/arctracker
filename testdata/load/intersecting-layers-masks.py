# Name: IntersectingLayersMasks_standalone_script.py
# Description: Creates masking polygons at a specified
#              shape and size at the intersections of symbolized features. 
 
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
masking_layer = "roads.lyrx"
masked_layer = "buildings_poly.lyrx"
outpuf_fc = "cartography.gdb/transportation/ilm_polys"
reference_scale = "25000"
spatial_reference = arcpy.Describe(masking_layer).spatialReference
margin = "5 Points"
method = "CONVEX_HULL"
mask_for_non_placed_anno = "ALL_FEATURES"
attributes = "ALL"

# Execute Intersecting Layers Masks
arcpy.IntersectingLayersMasks_cartography(masking_layer,
                                          masked_layer,
                                          output_fc,
                                          reference_scale,
                                          spatial_reference,
                                          margin, method,
                                          mask_for_non_placed_anno,
                                          attributes)