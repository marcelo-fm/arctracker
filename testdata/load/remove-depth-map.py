# Tool in Reality Mapping toolbox 

# Import system modules 

import arcpy 

# Define input parameters. All depth map content will be removed if not specified in where_clause. 

in_mosaic_dataset= r"C:\CDM_RM.gdb\YVWD" 

# Execute 

arcpy.rm.RemoveDepthMap(in_mosaic_dataset)