# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Define input parameters
inFile = "C:/data/salinity.crf"
dimensionName = "Time"
dimensiondef = "ALL"
intervalkeyword = ''
variables = "temp"
arg_statistics_type = "DURATION"
min_value = 20
max_value = 25
multiple_occurrances_value = None
ignore_nodata = "NODATA"

# Execute 
# get the number of continous slices that have temperature value between 20 and 25
argStatOutput = FindArgumentStatistics(inFile, dimensionName, dimensiondef, intervalkeyword,
	variables, arg_statistics_type, min_value, max_value, multiple_occurrances_value, ignore_nodata)
	
# Save output
argStatOutput.save("C:/data/arg_statistics_output2.crf")