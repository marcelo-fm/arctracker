#---------------------------------------------------------------------------
# Name: DetectObjectsUsingDeepLearning_example02.py
# Requirements: ArcGIS Image Server
# Import system modules
import arcpy
# Set local variables
inImage = "https://myserver/rest/services/coconutFarmImage/ImageServer"
inModel = "https://myportal/sharing/rest/content/items/itemId"
outName = "detectedTrees"
modelArgs = "score_threshold 0.6;padding 0"
runNMS = "NMS"
confScoreField = "Confidence"
classVField = "Class"
maxOverlapRatio = 0.15 
# Execute Detect Objects Using raster analysis tool
arcpy.ra.DetectObjectsUsingDeepLearning(inImage, inModel, outName, modelArgs,
runNMS, confScoreField, ClassVField, maxOverlapRatio)