# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Define input parameters
in_multidimensional = r"C:\data\Landsat_time_series.crf"
change_bands = [0,1,2,3,4,5,6]
tmask_bands = [2,6]
chi_sq_threshold = 0.99
min_consecutive_observations = 3
update_frequency = 1

# Execute
changeAnalysisRaster = arcpy.ia.AnalyzeChangesUsingCCDC(
	in_multidimensional, change_bands, tmask_bands, chi_sq_threshold, 
	min_consecutive_observations, update_frequency) 

# Save output
changeAnalysisRaster.save(r"C:\data\Landsat_ChangeAnalysis.crf")