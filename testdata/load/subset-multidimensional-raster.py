# Import system modules
import arcpy
 
# Set local variables
in_multidimensional_raster = r"C:\data\MD_Ocean_data.crf"
out_multidimensional_raster =  r"C:\data\salinity_slice.crf"
variables = "salinity"
dimension_def = "BY_ITERATION"
dimension = "StdTime"
start_of_first_iteration = "2009-01-01"
end_of_first_iteration = "2009-01-10"
iteration_step = "1"
iteration_unit = "YEARS"
 
#Execute
 
arcpy.md.SubsetMultidimensionalRaster(in_multidimensional_raster, out_multidimensional_raster, variables, dimension_def, dimension, start_of_first_iteration, end_of_first_iteration, iteration_step, iteration_unit)