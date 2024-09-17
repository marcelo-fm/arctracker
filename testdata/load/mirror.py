##====================================
##Mirror
##Usage: Mirror_management in_raster out_raster
    
import arcpy

arcpy.env.workspace = r"C:/Workspace"

##Mirror a TIFF format image
arcpy.Mirror_management("image.tif", "mirror.tif")