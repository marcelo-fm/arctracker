arcpy.MakeImageServerLayer_management(
        input2, "mdlayer", "feature.shp", "1;2;3",
        "LockRaster", "#", "#", "4", "#", processing_template="Custom_func")