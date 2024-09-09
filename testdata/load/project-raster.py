##====================================
##Project Raster
##Usage: ProjectRaster_management in_raster out_raster out_coor_system {NEAREST | BILINEAR 
##                                | CUBIC | MAJORITY} {cell_size} {geographic_transform;
##                                geographic_transform...} {Registration_Point} {in_coor_system}
    
import arcpy

arcpy.env.workspace = r"C:/Workspace"

##Reproject a TIFF image with Datumn transfer
arcpy.ProjectRaster_management("image.tif", "reproject.tif", "World_Mercator.prj",\
                               "BILINEAR", "5", "NAD_1983_To_WGS_1984_5", "#", "#")

##Reproject a TIFF image that does not have a spatial reference
##Set snapping point to the top left of the original image
snapping_pnt = "1942602 304176"

arcpy.ProjectRaster_management("nosr.tif", "project.tif", "World_Mercator.prj", "BILINEAR",\
                               "5", "NAD_1983_To_WGS_1984_6", snapping_pnt,\
                               "NAD_1983_StatePlane_Washington_North.prj")