# Name: SnapTracks.py
# Description: Snap snowplow fleet tracks to roads to uncover areas that 
#              may need more resources for snow removal efforts

# Import system modules
import arcpy

# Enable time on the input features using an .lyrx file.
# To create the .lyrx file, add your layer to a map, open the layer properties 
# and enable time. Then right-click the layer and select Share As Layer File.
inputLyrx = r'C:\data\Snowplow.lyrx'

# MakeFeatureLayer converts the .lyrx to features
snowplowsLayer = arcpy.management.MakeFeatureLayer(inputLyrx, "Snowplows Layer")

# ApplySymbologyFromLayer sets the time using the .lyrx file definition
arcpy.management.ApplySymbologyFromLayer(snowplowsLayer, inputLyrx)

# Set local variables
lineLayer = "c:/mydata/Roads.gdb/CityStreets"
trackIdentifier = "vehicle_id"
out = "c:/mydata/OutputDatasets.gdb/Snowplows_snapped_to_streets"
searchDistance = "10 Meters"
connectivityFieldMatching = "unique_ID from_node to_node"
directionValueMatching = "dir_travel F T B #"

# Run Snap Tracks
arcpy.gapro.SnapTracks(snowplowsLayer, lineLayer, out, trackIdentifier, 
                       searchDistance, connectivityFieldMatching, None,
																							"GEODESIC", directionValueMatching, "MATCHED_FEATURES")