# Import system modules
import arcpy
 
# Set local variables
in_multidimensional_raster = r"C:\data\MD_Ocean_data.crf"
out_multidimensional_raster_layer =  r"C:\data\salinity_slice.crf"
variables = "salinity"
dimension_def = "BY_ITERATION"
dimension = "StdTime"
start_of_first_iteration = "2009-01-01"
end_of_first_iteration = "2009-01-10"
iteration_step = "1"
iteration_unit = "YEARS"
template = "120.084279939743 0.914964278021376 139.524470909773 21.1231086159414"
 
#Execute
 
arcpy.md.MakeMultidimensionalRasterLayer(
	in_multidimensional_raster, out_multidimensional_raster_layer, 
	variables, dimension_def, dimension, start_of_first_iteration, 
	end_of_first_iteration, iteration_step, iteration_unit, template)