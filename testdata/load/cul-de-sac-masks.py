# Name: CulDeSacMasks_standalone_script.py
# Description: Creates masks at the unconnected ends of lines in the input layer. 
 
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
input_layer = "cartography.gdb/transportation/roads"
outpuf_fc = "cartography.gdb/transportation/cds_polys"
reference_scale = "25000"
spatial_reference = arcpy.Describe(input_layer).spatialReference
margin = "5 meters"
attributes = "ALL"

# Execute Cul De Sac Masks
arcpy.CulDeSacMasks_cartography(input_layer, output_fc, reference_scale, 
                                spatial_reference, margin, attributes)