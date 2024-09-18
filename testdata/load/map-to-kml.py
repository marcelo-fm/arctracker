# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Use ListFiles to identify all map files in workspace
files = arcpy.ListFiles('*.mapx') 
if len(files) > 0:
    for map_file in files:
        # Set Local Variables
        composite = 'NO_COMPOSITE'
        vector = 'VECTOR_TO_VECTOR'
        pixels = 2048
        dpi = 96
        clamped = 'ABSOLUTE'
        for scale in range(10000, 20000, 30000):
            # Strips the '.mapx' part of the name and appends '.kmz'
            outKML = map_file[:-5]+'.kmz'

            # Run MapToKML	
            arcpy.conversion.MapToKML(map_file, outKML, scale, composite, 
                                      vector, '', pixels, dpi, clamped)
else:
    arcpy.AddMessage('There are no map files (*.mapx) in {}.'.format(arcpy.env.workspace))