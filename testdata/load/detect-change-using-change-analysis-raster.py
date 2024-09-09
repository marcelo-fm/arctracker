# Import system modules
import arcpy
from arcpy.ia import *

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Define input parameters
in_change_analysis = r"C:\data\Landsat_ChangeAnalysis.crf"
change_type = "NUM_OF_CHANGES"

# Execute
number_of_changes = arcpy.ia.DetectChangeUsingChangeAnalysis(
	in_change_analysis, change_type)

# Save output
number_of_changes.save("C:/data/NumberOfChanges_Landsat.crf")