# Name: SubsetFeatures_Example_02.py
# Description: Randomly split the features into two feature classes.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
outtrainPoints = "C:/gapyexamples/output/training.shp"
outtestPoints = ""
trainData = ""
subsizeUnits = "PERCENTAGE_OF_INPUT"

# Execute SubsetFeatures
arcpy.SubsetFeatures_ga(inPointFeatures, outtrainPoints, outtestPoints, 
                        trainData, subsizeUnits)