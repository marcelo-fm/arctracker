'''====================================
Get Cell Value
Usage: GetCellValue_management in_raster location_point {ID;ID...}
'''   
   
import arcpy
arcpy.env.workspace = "C:/Workspace"

# Get the Band_2 and Band_3 cell value of certain point in a RGB image
result = arcpy.GetCellValue_management("rgb.img", "480785 3807335", "2;3")
cellvalue = int(result.getOutput(0))

# View the result in execution log
print(cellvalue)