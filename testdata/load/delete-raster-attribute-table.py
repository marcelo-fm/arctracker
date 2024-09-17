##====================================
##Delete Raster Attribute Table
##Usage: DeleteRasterAttributeTable_management in_raster
    
import arcpy
arcpy.env.workspace = "C:/Workspace"

##Delete the attribute table of single band image if exist
arcpy.DeleteRasterAttributeTable_management("image.tif")