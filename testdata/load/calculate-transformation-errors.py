import arcpy
import os

# All input data is in country.gdb and output will also go to this gdb
arcpy.env.workspace = os.path.join(os.getcwd(), "country.gdb")

in_links_feats = "link_features"
out_link_table = "output_table"

# Transformation method
method = "SIMILARITY"

result = arcpy.edit.CalculateTransformationErrors(in_links_feats, out_link_table, method)

# Get the transformation error
error = float(result.getOutput(1))

# If error is less than 12.234, run Transform Features
if error < 20.0:
    # Make a copy of the input features 
    arcpy.management.CopyFeatures(in_links_feats, "in_links_copy")
    arcpy.edit.TransformFeatures("in_links_copy", in_links_feats, method, "out_link_table")
else:
    print("Transformation error {} is too high".format(error))