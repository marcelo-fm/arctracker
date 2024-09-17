##====================================
##Raster Compare
##Usage: RasterCompare_management in_base_raster in_test_raster {RASTER_DATASET |
##                                GDB_RASTER_DATASET | GDB_RASTER_CATALOG |
##                                MOSAIC_DATASET} {ignore_option;ignore_option...}
##                                {NO_CONTINUE_COMPARE | CONTINUE_COMPARE} 
##                                {out_compare_file} {Parameter {Tolerance} {Type};
##                                Parameter {Tolerance} {Type}...} {Field {Tolerance};
##                                Field {Tolerance}...} {omit_field;omit_field...} 
    
    
try:
    import arcpy
    
    arcpy.env.workspace = "c:/workspace"
    
    ##Compare two Raster dataset
    arcpy.RasterCompare_management("raster_base.tif","raster_test.tif","RASTER_DATASET",\
                                   "","CONTINUE_COMPARE","compareresult.txt","","","")
    
    ##Compare two Raster Catalog with ignore options
    arcpy.RasterCompare_management("fgdb.gdb/rc_base","fgdb.gdb/rc_test","RASTER_CATALOG",\
                                   "IsManaged;Extent","CONTINUE_COMPARE","compareresult2.txt",\
                                   "","","DATE")
    
    ##Compare two Mosaic Dataset with torelance
    arcpy.RasterCompare_management("fgdb.gdb/md_base","fgdb.gdb/md_test","MOSAIC_DATASET",\
                                   "IsEmbedded;Seamline","CONTINUE_COMPARE","compareresult3.txt",\
                                   "All 0.00001 Fraction","HighPS 0.0001;LowPS 0.0001",\
                                   "ItemTS;UriHash")
    
except:
    print "Raster Compare exsample failed."
    print arcpy.GetMessages()