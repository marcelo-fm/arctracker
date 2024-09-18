# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Define input parameters
inFile = "C:/data/landsat7_image.crf"
training_features = "C:/data/training_features.shp"
options = "SUM_TO_ONE;NON_NEGATIVE" 

# Execute 
unmixing_outputs = LinearSpectralUnmixing(inFile, training_features, options)
	
# Save output
unmixing_outputs.save("C:/data/unmixing_outputs_using_training_features.crf")