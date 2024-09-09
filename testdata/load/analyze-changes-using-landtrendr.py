# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Define input parameters
in_multidimensional = r"C:\data\Landsat_time_series.crf"
processing_band = "Band_4"
snapping_date = ""
max_num_segments = 10
vertex_count_overshoot = 3
spike_threshold = 0.9
recovery_threshold = 0.25
prevent_one_year_recovery = "PREVENT_ONE_YEAR_RECOVERY"
recovery_trend = "INCREASING_TREND"
min_num_observations = 6
best_model_proportion = 1.25
pvalue_threshold = 0.01
output_other_bands = "EXCLUDE_OTHER_BANDS"

# Execute
changeAnalysisRaster = arcpy.ia.AnalyzeChangesUsingCCDC(
	in_multidimensional, processing_band, snapping_date, max_num_segments,
	vertex_count_overshoot, spike_threshold, recovery_threshold, prevent_one_year_recovery,
	recovery_trend, min_num_observations, best_model_proportion, pvalue_threshold, output_other_bands)

# Save output
changeAnalysisRaster.save(r"C:\data\Landsat_ChangeAnalysis.crf")