# Name: JoinFeatures.py
# Description: Join crime events that are close together in time and space, and 
#              return the count of nearby crimes. This example is a self join 
#              (joining the same layer to itself).

# Import system modules 
import arcpy 

arcpy.env.workspace = "C:/data/CityData.gdb"

# Enable time on the input features using an .lyrx file.
# To create the .lyrx file, add your layer to a map, open the layer properties 
# and enable time. Then right-click the layer and select Share As Layer File.
inputLyrx = r'C:\data\ChicagoCrimes.lyrx'

# MakeFeatureLayer converts the .lyrx to features
chicagoCrimesLayer = arcpy.management.MakeFeatureLayer(inputLyrx, "Crimes_layer")

# ApplySymbologyFromLayer sets the time using the .lyrx file definition
arcpy.management.ApplySymbologyFromLayer(chicagoCrimesLayer, inputLyrx)

# Set local variables
spatialOperation = "NEAR" 
nearDistance = "1 Kilometers" 
temporalOperation = "NEAR" 
nearTime = "3 Hours" 
out = "CloseCrimes"

# Run Join Features
arcpy.gapro.JoinFeatures(chicagoCrimesLayer, inFeatures, out, "JOIN_ONE_TO_ONE", 
                         spatialOperation, nearDistance, temporalOperation, 
                         nearTime)