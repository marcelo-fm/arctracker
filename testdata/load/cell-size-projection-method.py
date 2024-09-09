import arcpy

# Set the workspace, Output Coordinate System and Cell Size Projection Method 
# environments
arcpy.env.workspace = "C:/workspace"
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 18N")

# Set Cell Size Projection Method environment
arcpy.env.cellSizeProjectionMethod = "PRESERVE_RESOLUTION"

# Set local variables
InZones = "C:/data/parcels.shp"
InZoneField = "Parcel_ID"
InValueRaster = "C:/data/Slope"

# Check out a Spatial Analyst license
arcpy.CheckOutExtension("Spatial")

# Process: Calculate the mean slope of each parcel area.
out = arcpy.sa.ZonalStatistics(InZones, InZoneField, InValueRaster, "MEAN", "DATA")
out.save("mean_ParSlp")