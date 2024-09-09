import arcpy
arcpy.env.workspace = 'C:/project_directory'

# Export the feature class or layer to model files on disk
arcpy.management.Export3DObjects("city_models.gdb/Downtown_Buildings", 
                                 "exported_models", ["FMT3D_IFC"])

# Optionally, edit the exported model files in other software, or replace the 
# files with a new version. 
# Keep the file names the same to update existing features. New file names are
# interpreted as new features.

# The input folder and feature class or layer in Import 3D Objects are the same
# values used in Export 3D Objects.
arcpy.management.Import3DObjects("exported_models", 
                                 "city_models.gdb/Downtown_Buildings", 
                                 update="UPDATE_EXISTING_ADD_NEW", 
                                 translate="350 150",
                                 elevation=100, scale=2.54, rotate=-90)