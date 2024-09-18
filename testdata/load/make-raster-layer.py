##====================================
##Make Raster Layer
##Usage: MakeRasterLayer_management in_raster out_rasterlayer {where_clause} {envelope}
##                                  {Index;Index...}
    
import arcpy

arcpy.env.workspace = r"C:/Workspace"

##Create raster layer from single raster dataset with clipping feature
arcpy.MakeRasterLayer_management("image.tif", "rdlayer", "#", "feature.shp", "1")