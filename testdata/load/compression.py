import arcpy

# Set the compression environment to LZ77
arcpy.env.compression = "LZ77"

# Set the compression environment to JPEG with a quality of 80
arcpy.env.compression = "JPEG 80"