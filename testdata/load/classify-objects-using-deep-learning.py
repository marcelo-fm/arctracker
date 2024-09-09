#---------------------------------------------------------------------------
# Name: ClassifyObjectsUsingDeepLearning_example02.py
# Requirements: ArcGIS Image Server
# Import system modules
import arcpy

# Set local variables
inputRaster = "https://myserver/rest/services/Buildings/ImageServer"
inputFeatures = "https://myserver/rest/services/Hosted/BuildingFootprints/FeatureServer/0"
inputModel = "https://myportal/sharing/rest/content/items/itemId"
outputName = "BuildingDamage"
modelArguments = "batch_size 4"
classLabelField = "ClassLabel"
processingMode = "PROCESS_AS_MOSAICKED_IMAGE"

# Execute Classify Objects Using Deep Learning 
arcpy.ra.ClassifyObjectsUsingDeepLearning(inputRaster, inputFeatures, 
	inputModel, outputName, modelArguments, classLabelField , processingMode)