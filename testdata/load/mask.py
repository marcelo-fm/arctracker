import arcpy

# Set environment
arcpy.env.workspace = "C:/workspace"
arcpy.env.extent = "C:/data/StudyArea.tif"
arcpy.env.snapRaster = "C:/data/slope_ras.tif"

# Set Mask environment
arcpy.env.mask = "C:/data/maskpoly.shp"

# Set local variables
InZones = "C:/data/parcels.shp"
InZoneField = "Parcel_ID"
InValueRaster = "C:/data/slope_ras.tif"

# Check out a Spatial Analyst license
arcpy.CheckOutExtension("Spatial")

# Process: Calculate the mean slope of each parcel area.
out = arcpy.sa.ZonalStatistics(InZones, InZoneField, InValueRaster, "MEAN", 
                               "DATA")
out.save("mean_ParSlp.tif")