import arcpy
arcpy.intelligence.GenerateBlindSpotAreas("bs_buffer2", "mtyBS001", "mask", 
                                          "time_start", "time_end")