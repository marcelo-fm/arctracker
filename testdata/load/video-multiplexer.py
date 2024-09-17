import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

in_video = "c:\\test\\drone_vid.mpeg"
in_metadata = "c:\\test\\videometadata.csv"
out_video = "c:\\test\\mutiplexer_output.ts"
MISB_mapping = "c:\\test\\Field_Mapping_Template.csv"
time_shift_file = "c:\\test\\timeshift.csv"
in_elevation_layer = "c:\\test\\dem.tif"

arcpy.ia.VideoMultiplexer(in_video, in_metadata, out_video, MISB_mapping, time_shift_file, in_elevation_layer)