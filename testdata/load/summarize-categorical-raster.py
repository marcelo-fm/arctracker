# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Define input parameters
inputRaster = "C:/Data/YearlyFireRisk.crf"
outputTable = "C:/Data/FireRiskSummary.csv"
dimension = "StdTime"
aoi = "C:/Data/MyData.gdb/SanBernardinoMountainRange"
aoi_id_field = "WATERSHEDS"

# Execute

arcpy.ia.SummarizeCategoricalRaster(inputRaster, outputTable, dimension, aoi, aoi_id_field)