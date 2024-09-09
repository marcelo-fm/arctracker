import arcpy

# Set the extent environment using a keyword
arcpy.env.extent = "MAXOF"

# Set the extent environment using the Extent class
arcpy.env.extent = arcpy.Extent(-107.0, 38.0, -104.0, 40.0)

# Set the extent environment using a space-delimited string
arcpy.env.extent = "-107.0 38.0 -104.0 40.0"

# Set the extent environment using a feature class
arcpy.env.extent = "C:/data/StudyArea_perim.shp"

# Set the extent environment using a raster
arcpy.env.extent = "C:/data/StudyArea.tif"