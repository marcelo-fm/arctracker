## Build multidimensional information for a mosaic dataset 
## containing sea ice extent imagery over time and water depth.

import arcpy
arcpy.env.workspace = "C:/data"

## Define the input parameters
inputmosaicdataset = "input.gdb/seaice_1982_2019"
variable_field = "measurement"
dimension_fields= "AcquisitionDate;Depth"

arcpy.md.BuildMultidimensionalInfo(
	inputmosaicdataset, variable_field, 
	dimension_fields)