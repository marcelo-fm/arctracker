# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Define input parameters
inFile = "C:/Data/HarmonicTrendCoefficients.crf"
variables = "NDVI"
dimension_definition = "BY_INTERVAL"
start = "2025-01-01T00:00:00"
end = "2025-12-31T00:00:00"
interval_value = 1
interval_unit = "MONTHS"

# Execute - predict the monthly NDVI in 2025 
predictOutput = PredictUsingTrendRaster(inFile, variables, 
	dimension_definition, '', start, end, interval_value, interval_unit)
	
# Save output
predictOutput.save("C:/data/predicted_ndvi.crf")