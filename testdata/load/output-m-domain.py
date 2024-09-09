import arcpy

# Set the MResolution first
arcpy.env.MResolution = 0.0001 

# Then set the MDomain (only the origin will be used when the resolution is set)
arcpy.env.MDomain = "0 10000000"