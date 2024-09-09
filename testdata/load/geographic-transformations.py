import arcpy

# Set the workspace, outputCoordinateSystem and geographicTransformations 
# environments
arcpy.env.workspace = "c:/data"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 18N")
arcpy.env.geographicTransformations = "Arc_1950_To_WGS_1984_5; PSAD_1956_To_WGS_1984_6"

arcpy.analysis.Buffer("roads.shp", "roads_buffer.shp", "10 meters")