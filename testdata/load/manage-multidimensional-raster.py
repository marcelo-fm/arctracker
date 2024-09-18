# Import system modules
import arcpy

# Define input parameters
target_multidimensional_raster = "C:/data/precip.crf"
manage_mode = "REMOVE_DIMENSION"

# Remove dimension to make input data dimensionless
arcpy.md.ManageMultidimensionalRaster(target_multidimensional_raster,
	manage_mode)