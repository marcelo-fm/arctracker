### InspectTrainingSamples example 2 (stand-alone script)
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

out_misclassified_raster = InspectTrainingSamples("C:/Data/wv2.tif", 
                                                  "C:/out/ts.shp", 
                                                  "C:/Data/svm.ecd", 
                                                  "C:/out/ts2.shp", 
                                                  "C:/Data/seg.tif"); 
out_misclassified_raster.save("C:/temp/misclassified.tif")