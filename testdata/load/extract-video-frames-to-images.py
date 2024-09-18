import arcpy
from arcpy.ia import *

arcpy.CheckOutExtension("ImageAnalyst")

in_video = "c:\\test\\drone_vid.ts"
out_folder = "c:\\output"
outformat = "NITF"
maxoverlap = 100
requirefreshmeta = “REQUIRE_FRESH_METADATA” 
mintimebetween = "1 minute"


arcpy.ia.ExtractVideoFramesToImages(in_video, out_folder, outformat, maxoverlap,
requirefreshmeta, mintimebetween)