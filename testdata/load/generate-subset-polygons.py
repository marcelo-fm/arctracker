# Name: GenerateSubsetPolygons_Example_02.py
# Description: Groups points into polygon subsets of a similar size.
# Requirements: Geostatistical Analyst Extension
# Author: Esri

# Import system modules
import arcpy

# Set local variables
inPoints = "C:/gapyexamples/input/myPoints.shp"
outFeatureClass = "C:/gapyexamples/output/myPolygons.shp"
minPoints = 50
maxPoints = 75
coincidentPoints = "COINCIDENT_ALL"

# Check out the ArcGIS Geostatistical Analyst extension license
arcpy.CheckOutExtension("GeoStats")

# Execute GenerateSubsetPolygons
arcpy.ga.GenerateSubsetPolygons(inPoints, outFeatureClass, minPoints, maxPoints, coincidentPoints)