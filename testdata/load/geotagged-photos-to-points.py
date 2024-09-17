"""Name: GeoTaggedPhotosToPoints example
Description: Convert a folder of photos to points, then perform a buffer
""" 

# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data"
 
# Set local variables
inFolder = "photos"
outFeatures = "city.gdb/photos_points"
badPhotosList = "city.gdb/photos_noGPS"
photoOption = "ONLY_GEOTAGGED"
attachmentsOption = "ADD_ATTACHMENTS"

buffers = "city.gdb/photos_points_buffer"
bufferDist = "1 Miles"

arcpy.management.GeoTaggedPhotosToPoints(inFolder, outFeatures, badPhotosList, 
                                         photoOption, attachmentsOption)
arcpy.analysis.Buffer(outFeatures, buffers, bufferDist)