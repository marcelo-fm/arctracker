import arcpy
arcpy.ba.MeasureCannibalization("SF_Stores_Rings", "AREA_ID", "AREA_DESC",
                                r"C:\ MyProject1\MyProject1.gdb\SF_Stores_RIngs_MeasureCannibalization",
                                "STORE_ID", "CREATE_REPORT",
                                "Measure Cannibalization",
                                r"C:\ MyProject1\MeasureCannibalization", "PDF")