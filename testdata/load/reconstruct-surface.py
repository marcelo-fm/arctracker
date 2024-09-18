#ReconstructSurface example 3 (stand-alone script) 
#This example creates multiple 2D products from aerial nadir imagery. 

# Import system modules 
import arcpy 

# Define input parameters 
in_mosaic = "C:/ReconstructSurface.gdb/aerialMD" 
out_folder = "C:/ScenarioAerialNadir" 
json_file = "" 
scenario = "AERIAL_NADIR" 
forward_overlap = 60
side_overlap = 30 
out_quality = "ULTRA" 
output_products = "DSM;TRUE_ORTHO;DSM_MESH" 

#Execute - Generate Products 
products = arcpy.rm.ReconstructSurface(in_mosaic, out_folder, json_file,senario, forward_overlap, side_overlap, out_quality, output_products)