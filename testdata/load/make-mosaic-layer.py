arcpy.MakeMosaicLayer_management(
        "fgdb.gdb/mdsrc", "mdlayer2", "", "clipmd.shp", "3;2;1", 
		"BY_ATTRIBUTE", "Tag", "Dataset", "", "DESCENDING", "LAST", "10", 
		processing_template="Custom_func")