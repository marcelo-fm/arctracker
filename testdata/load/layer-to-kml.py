# Description: The following stand-alone script demonstrates how to find 
#              all layer files in a given workspace and export each to 
#              a KML at the 1:10,000, 1:20,000, and 1:30,000 scale using
#              the LayerToKML tool.
import arcpy

arcpy.env.workspace = "C:/data"

# Set Local Variables
composite = 'NO_COMPOSITE'
pixels = 2048
dpi = 96
clamped = 'CLAMPED_TO_GROUND'

# Use the ListFiles method to identify all lyr and lyrx files in workspace
layers = arcpy.ListFiles("*.lyr*") 

if len(layers) > 0:
    for layer in layers:        
        # Strips the '.lyr(x)' part of the name and appends '.kmz'
        outKML = os.path.join(os.path.splitext(layer), ".kmz")
        for scale in range(10000, 30001, 10000):
            # Run LayerToKML
            arcpy.conversion.LayerToKML(layer, outKML, scale, composite, 
                                        '', pixels, dpi, clamped)
else:
    arcpy.AddMessage('There are no layer files in {}'.format(arcpy.env.workspace))