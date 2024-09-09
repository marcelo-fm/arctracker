import arcpy

# Set the pyramid environment to build all pyramids levels with cubic 
# convolution resampling, LZ77 compression
arcpy.env.pyramid = "PYRAMIDS -1 CUBIC LZ77 NO_SKIP"