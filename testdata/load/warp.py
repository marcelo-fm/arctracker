##====================================
##Warp
##Usage: Warp_management in_raster source_control_points;source_control_points... 
##                       target_control_points;target_control_points... out_raster
##                       {POLYORDER_ZERO | POLYORDER1 | POLYORDER2 | POLYORDER3 | 
##                       ADJUST | SPLINE | PROJECTIVE} {NEAREST | BILINEAR | 
##                       CUBIC | MAJORITY}
    

import arcpy

arcpy.env.workspace = r"C:/Workspace"

##Warp a TIFF raster dataset with control points
##Define source control points
source_pnt = "'234718 3804287';'241037 3804297';'244193 3801275'"

##Define target control points
target_pnt = "'246207 3820084';'270620 3824967';'302634 3816147'"

arcpy.Warp_management("raster.img", source_pnt, target_pnt, "warp.tif", "POLYORDER2",\
                      "BILINEAR")