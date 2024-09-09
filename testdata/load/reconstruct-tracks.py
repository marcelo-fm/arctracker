# Name: ReconstructTracks.py
# Description: Reconstruct hurricane points into hurricane tracks, where each 
#              location is buffered by the wind speed * 100.

# Import system modules
import arcpy

# Enable time on the input features using an .lyrx file.
# To create the .lyrx file, add your layer to a map, open the layer properties 
# and enable time. Then right-click the layer and select Share As Layer File.
inputLyrx = r'C:\data\Hurricanes.lyrx'

# MakeFeatureLayer converts the .lyrx to features
hurricanesLayer = arcpy.management.MakeFeatureLayer(inputLyrx, "Hurricanes Layer")

# ApplySymbologyFromLayer sets the time using the .lyrx file definition
arcpy.management.ApplySymbologyFromLayer(hurricanesLayer, inputLyrx)

# Set local variables
trackIdentifier = "EVENTID"
out = "c:/mydata/OutputDatasets.gdb/HurricaneTracks"
bufferExpression = "WINDSPEED * 100"
statistics = [["PRESSURE", "MEAN"]]

# Run Reconstruct Tracks
arcpy.gapro.ReconstructTracks(hurricanesLayer, out, trackIdentifier, 
                              "GEODESIC", "EXPRESSION", None, 
                              bufferExpression, None, statistics)