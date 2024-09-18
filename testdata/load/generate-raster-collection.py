import arcpy
arcpy.GenerateRasterCollection_management(
    out_raster_collection="c:/temp/FGDB.gdb/testgencollection", 
    collection_builder="Simple Collection", 
    collection_builder_arguments="# DataSource c:\temp\FGDB.gdb\qb_portland;# 
WhereClause 'Tag = 'MS''", 
    raster_function="C:/temp/NDVI_test.rft.json", 
    raster_function_arguments="# MS #;# VisibleBandID_20171019_7337_958 1;# 
InfraredBandID_20171019_7337_958 4", 
    collection_properties="", 
    generate_rasters="GENERATE_RASTERS", 
    out_workspace="c:/temp/persistedoutput", 
    format="CRF"
)