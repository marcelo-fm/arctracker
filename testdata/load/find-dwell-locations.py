# Name: FindDwellLocations.py
# Description: Find the mean centers representing locations where ships have 
#              stayed within 1 mile across 4 hours of travel.

# Requirements: ArcGIS GeoAnalytics Desktop tools

# Import system modules
import arcpy

# Enable time on the input features using an .lyrx file.
# To create the .lyrx file, add your layer to a map, open the layer properties 
# and enable time. Then right-click the layer and select Share As Layer File.
inputLyrx = r'C:\data\MyAtlanticShips.lyrx'

# MakeFeatureLayer converts the .lyrx to features
myAtlanticShipsInputLayer = arcpy.management.MakeFeatureLayer(inputLyrx, "MyAtlanticShips_layer")

# ApplySymbologyFromLayer sets the time using the .lyrx file definition
arcpy.management.ApplySymbologyFromLayer(myAtlanticShipsInputLayer, inputLyrx)

# Set local variables
outFeatures = "c:/mydata/OutputDatasets/AtlanticShips_DwellLocations.shp"
trackIdentifier = "SHIPID"
distance = "1 Miles"
timeDuration = "4 Hours"
outputType = "MEAN_CENTERS"
statistics = [["SPEED", "MEAN"]]

# Run Find Dwell Locations
arcpy.gapro.FindDwellLocations(myAtlanticShipsInputLayer, outFeatures, trackIdentifier, 
                               "GEODESIC", distance, timeDuration, 
                               outputType, statistics)