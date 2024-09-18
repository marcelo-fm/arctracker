##====================================
##Rescale
##Usage: Usage: Rescale_management in_raster out_raster x_scale y_scale
    
import arcpy

arcpy.env.workspace = r"C:/Workspace"

##Rescale a TIFF image by a factor of 4 in both directions
arcpy.Rescale_management("image.tif", "rescale.tif", "4", "4")