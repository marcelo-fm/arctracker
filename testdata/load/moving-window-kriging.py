# Name: MovingWindowKriging_Example_02.py
# Description: The kriging model is automatically estimated for each neighborhood
#              as the kriging interpolation moves through all the location points.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inLayer = "C:/gapyexamples/data/kriging.lyr"
inPoints = "C:/gapyexamples/data/ca_ozone_pts.shp OZONE"
obsPoints = "C:/gapyexamples/data/obs_pts.shp"
maxNeighbors = 10
outPoints = "C:/gapyexamples/output/outMWK"

# Execute MovingWindowKriging
arcpy.GAMovingWindowKriging_ga(inLayer, inPoints, obsPoints, maxNeighbors,
                               outPoints)