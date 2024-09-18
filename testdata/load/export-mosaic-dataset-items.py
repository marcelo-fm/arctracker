#Export Mosaic Dataset items
                                                                       
import arcpy
arcpy.env.workspace = "c:/workspace"
    
#export mosaic dataset items using feature class as clipping extent
imdname = "exportmditem.gdb/exportmd" 
outfolder = "c:/workspace/outfolder"
basename = "Landsat8"
query = "OBJECTID = 1"
out_format = "TIFF"
nodata_value = "#"
cliptype = "FEATURE_CLASS"
clip_featureclass = "c:/workspace/featureclassdb.gdb/clip_FC"
cell_size = "#"

arcpy.ExportMosaicDatasetItems_management(imdname, outfolder, basename, 
     query, out_format, nodata_value, cliptype, clip_featureclass, cell_size)