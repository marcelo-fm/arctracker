# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Define input parameters

inFile = "C:/data/ndvi_time_series.crf"
dimensionName = "StdTime"
variables = "ndvi"
trend_test = "SEASONAL_KENDALL"
trend_model = "HARMONIC"
harmonic_frequency = 1
ignore_Nodata = "DATA"
length_of_cycle = 365.25
rmse = RMSE
r_square = NO_r2
p_value = NO_SLOPEPVALUE

# Test for monotonic trend 

trendtest = GenerateTrendRaster(inFile, dimensionName, variables,
	trend_test, '', ignore_Nodata, '', '', '', '', '', 'MONTHS')

# Execute 
trendCoeffMultidim = GenerateTrendRaster(inFile, dimensionName, 
	variables, trend_model, harmonic_frequency, ignore_nodata,
	length_of_cycle,rmse,r_square,p_value)
	
# Save output
trendCoeffMultidim.save("C:/data/harmonic_trend_coefficients.crf")