# Name: CalculateDensity.py
# Description: Calculate density using the count of points as well as the severity 
#              value of outbreaks by week.

# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/HealthInfo.gdb"

# Enable time on the input features using an .lyrx file.
# To create the .lyrx file, add your layer to a map, open the layer properties 
# and enable time. Then right-click the layer and select Share As Layer File.
inputLyrx = r'C:\data\outbreaks.lyrx'

# MakeFeatureLayer converts the .lyrx to features
outbreaksLayer = arcpy.management.MakeFeatureLayer(inputLyrx, "outbreaks_layer")

# ApplySymbologyFromLayer sets the time using the .lyrx file definition
arcpy.management.ApplySymbologyFromLayer(outbreaksLayer, inputLyrx)

# By default, the count of points will be used in addition to any other fields 
# that are specified
fields = "Severity"

# Set the size of bins and neighborhood and the time step size
binSize = "1 Kilometers"
neighborhoodSize = "2 Kilometers"
timeStepInterval = "1 Weeks"

# Specify output info
out = "OutbreakDensity"


# Run Calculate Density
arcpy.gapro.CalculateDensity(outbreaksLayer, out, 'HEXAGON', binSize, 
                             'UNIFORM', neighborhoodSize, fields, 
                             'SQUARE_KILOMETERS', timeStepInterval)