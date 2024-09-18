##====================================
##Rotate
##Usage: Rotate_management in_raster out_raster angle {pivot_point} {NEAREST | BILINEAR | CUBIC | MAJORITY}
    
import arcpy

arcpy.env.workspace = r"C:/Workspace"
pivot_point = "1942602 304176"

##Rescale a TIFF image by a factor of 4 in both directions
arcpy.Rotate_management("image.tif", "rotate.tif", "30", pivot_point, "BILINEAR")