# Import system modules
import arcpy

# Define input parameters
input_multidimensional_rasters = ["C:/data/hycom_East.crf", "C:/data/hycom_WEST.crf"]
output_multidimensional_raster = "C:/new_data/hycom_ALL.crf"


# Merge the spatial regions of the input data
arcpy.md.MergeMutidimensionalRaster(
	input_multidimensional_rasters, output_multidimensional_raster, "FIRST")