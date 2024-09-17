##====================================
##Flip
##Usage: Flip_management in_raster out_raster
    
import arcpy

arcpy.env.workspace = r"C:/Workspace"

##Flip a TIFF format image
arcpy.Flip_management("image.tif", "flip.tif")