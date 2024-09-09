# Import system modules 
import arcpy
from arcpy.ia import *

#Check out ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set local variables
in_raster = "C:/Data/LandSat8_SurfaceReflectance.tif"
in_spectra_file = "C:/Data/ref_spectra.shp"
method = "SID"
thresholds = .08
out_score_raster = "C:/Data/scoreSID.crf"
out_classifier_definition = "C:/Data/SID_classifier.ecd"

# Execute 
Classified_output = arcpy.ia.ClassifyRasterUsingSpectra(in_raster, in_spectra_file, method, thresholds, out_score_raster, out_classifier_definition)

# Save output
Classified_output.save("C:/data/Classified_output.crf")