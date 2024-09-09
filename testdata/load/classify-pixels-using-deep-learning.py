#---------------------------------------------------------------------------
# Name: ClassifyPixelsUsingDeepLearning_example02.py
# Requirements: ArcGIS Image Server
# Import system modules
import arcpy
# Set local variables
inImage = "https://myserver/rest/services/ landclassification/ImageServer"
inModel = "https://myportal/sharing/rest/content/items/itemId"
outName = "classifiedLand"
modelArgs = "padding 0"
# Execute Classified Pixels Using raster analysis tool
arcpy.ra.ClassifyPixelsUsingDeepLearning(inImage, inModel, outName, modelArgs)