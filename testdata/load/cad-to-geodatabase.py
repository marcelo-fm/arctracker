# Name: CADtoGeodatabase.py
# Description: Create a feature dataset

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/data"

# Set local variables
input_cad_dataset = "C:/data/City.DWG"
out_gdb_path = "C:/data/HabitatAnalysis.gdb" 
out_dataset_name = "analysisresults"
reference_scale = "1000"
spatial_reference = "NAD_1983_StatePlane_California_VI_FIPS_0406_Feet"

# Create a file geodatabase for the feature dataset
arcpy.management.CreateFileGDB("C:/data", "HabitatAnalysis.gdb")

# Run CreateFeaturedataset
arcpy.conversion.CADToGeodatabase(input_cad_dataset, out_gdb_path,
                                  out_dataset_name, reference_scale,
                                  spatial_reference)