# Description: Create a feature class to store the gnatcatcher habitat zones

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/data"

# Set local variables
out_path = "C:/output"
out_name = "habitatareas.shp"
geometry_type = "POLYGON"
template = "study_quads.shp"
has_m = "DISABLED"
has_z = "DISABLED"

# Use Describe to get a SpatialReference object
spatial_ref = arcpy.Describe("C:/workspace/studyarea.shp").spatialReference

# Run CreateFeatureclass
arcpy.management.CreateFeatureclass(out_path, out_name, geometry_type, template, 
                                    has_m, has_z, spatial_ref)