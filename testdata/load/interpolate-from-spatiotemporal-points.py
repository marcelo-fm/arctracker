# Import system modules
import arcpy
from arcpy import *

#Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Set local variables
in_dataset = "icesat_trajectory"
out_raster = r"C:\temp\icesat_surface.crf"
variable_field = "elevation"
time_field = "Time"
temporal_aggregation = "Daily"
cell_size = 5000
interpolation_method = "Quadratic"

# Execute
interpolation_output = arcpy.ia.InterpolateFromSpatiotemporalPoints(in_dataset, out_raster, variable_field,
		       time_field, temporal_aggregation, cell_size, interpolation_method)