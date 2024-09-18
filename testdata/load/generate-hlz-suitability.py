import arcpy
arcpy.intelligence.GenerateHLZSuitability("d:/working/monterey/working_mty/results.gdb/ned_reclass_10m", 
                                          "d:/working/monterey/working_mty/results.gdb/nlcd_reclass_10m", 
                                          "d:/working/monterey/working_mty/results.gdb/obx_buffers", 
                                          "d:/working/monterey/working_mty/results.gdb/monterey_hlz")