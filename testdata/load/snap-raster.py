import arcpy

# Set workspace and extent environments
arcpy.env.workspace = "C:/workspace"
arcpy.env.extent = "C:/data/StudyArea.tif"

# Set Snap Raster environment
arcpy.env.snapRaster = "C:/data/my_snapraster.tif"

# Set local variables
InZones = "C:/data/parcels.shp"
InZoneField = "Parcel_ID"
InValueRaster = "C:/data/slope_ras.tif"

# Check out ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Process: Calculate the mean slope of each parcel area.
out = arcpy.sa.ZonalStatistics(InZones, InZoneField, InValueRaster, "MEAN", 
                               "DATA")
out.save("mean_ParSlp.tif")