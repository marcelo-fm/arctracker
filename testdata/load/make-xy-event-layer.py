# Description: Creates an XY layer and exports it to a layer file

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"
 
# Set the local variables
in_Table = "firestations.dbf"
x_coords = "POINT_X"
y_coords = "POINT_Y"
z_coords = "POINT_Z"
out_Layer = "firestations_layer"
saved_Layer = r"c:\output\firestations.lyr"

# Set the spatial reference
spRef = r"NAD_1983_UTM_Zone_11N"

# Make the XY event layer...
arcpy.management.MakeXYEventLayer(in_Table, x_coords, y_coords, out_Layer, 
                                  spRef, z_coords)

# Save to a layer file
arcpy.management.SaveToLayerFile(out_Layer, saved_Layer)