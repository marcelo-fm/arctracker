# Name: DetectIncidents.py
# Description: Detect incidents when wind speed is greater than 100 miles per hour

# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/Weather.gdb"

# Enable time on the input features using an .lyrx file.
# To create the .lyrx file, add your layer to a map, open the layer properties 
# and enable time. Then right-click the layer and select Share As Layer File.
inputLyrx = r'C:\data\Hurricanes.lyrx'

# MakeFeatureLayer converts the .lyrx to features
hurricanesLayer = arcpy.management.MakeFeatureLayer(inputLyrx, "Hurricanes Layer")

# ApplySymbologyFromLayer sets the time using the .lyrx file definition
arcpy.management.ApplySymbologyFromLayer(hurricanesLayer, inputLyrx)

# Set local variables
out = "Hurricane_Incidents"
trackIdentifier = "STAGE"
startCondition = "$feature['WINDSPEED'] > 100"

# Run Detect Incidents
arcpy.gapro.DetectIncidents(hurricanesLayer, out, trackIdentifier, startCondition)