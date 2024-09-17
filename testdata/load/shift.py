##====================================
##Shift
##Usage: Shift_management in_raster out_raster x_value y_value {in_snap_raster}
    
import arcpy

arcpy.env.workspace = r"C:/Workspace"

##Shift a TIFF image by 4.5 in X direction and 6 in Y direction
##Snap the output to a existing raster dataset
arcpy.Shift_management("image.tif", "shift.tif", "4.5", "6", "snap.tif")