import arcpy 

arcpy.ComputeCameraModel_rm("c:\data\fgdb.gdb\md", "output_DSM.tif", 
                                    "HIGH", "ESTIMATE", "REFINE", "APPLY", "5")