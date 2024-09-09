##====================================
##Build Raster Attribute Table
##Usage: BuildRasterAttributeTable_management in_raster {NONE | Overwrite}
    
import arcpy
arcpy.env.workspace = "C:/Workspace"

##Build attribute table for single band raster dataset
##Overwrite the existing attribute table file
arcpy.BuildRasterAttributeTable_management("image.tif", "Overwrite")