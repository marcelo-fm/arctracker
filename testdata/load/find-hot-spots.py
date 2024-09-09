# Name: FindHotSpots.py
# Description: Find Hots Spots of 311 calls for bins of 500 meters looking at 
# neighbors within 1 kilometer. Complete the analysis for each month. 

# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/Calls311.gdb"

# Enable time on the input features using an .lyrx file.
# To create the .lyrx file, add your layer to a map, open the layer properties 
# and enable time. Then right-click the layer and select Share As Layer File.
input_lyrx = r'C:\data\SanFrancisco_311calls.lyrx'

# MakeFeatureLayer converts the .lyrx to features
SF311CallsInputLayer = arcpy.management.MakeFeatureLayer(input_lyrx, "SF_311Calls_layer")

# ApplySymbologyFromLayer sets the time using the .lyrx file definition
arcpy.management.ApplySymbologyFromLayer(SF311CallsInputLayer, input_lyrx)

# Set local variables
bins = "500 Meters"
neighborhood = "1 Kilometers"
timeStep = "1 Months"
out = "HotSpotsOf311Data"

# Run Find Hot Spots
arcpy.gapro.FindHotSpots(SF311CallsInputLayer, out, bins, neighborhood, timeStep)