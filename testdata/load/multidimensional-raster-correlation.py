# Import system modules 
import arcpy 
from arcpy.ia import * 

# Check out the ArcGIS Image Analyst extension license 
arcpy.CheckOutExtension("ImageAnalyst") 

# Define input parameters
raster1=r"E:\data\soil2022.crf"
raster2=r"E:\data\weather2022.crf"
dimension1="StdTime"
variable1="soilm"
dimension2="StdTime"
variable2="temperature"
correlation_method="PEARSON"
lag=3
calculate_cross_correlation="ALL_CROSS_CORRELATION"
calculate_pvalue="CACULATE_P_VALUE"
out_max_correlation_raster=r"E:\data\max_correlation.crf"

# Execute 
output = arcpy.ia.MultidimensionalRasterCorrelation(raster1, raster2, dimension1, variable1, dimension2, variable2, correlation _method, lag, calculate_cross_correlatio, calculate_pvalue, out_max_ correlation_raster)
output.save(r"E:\data\cross_correlation_raster.crf")