import arcpy

arcpy.intelligence.GenerateObstacleFeatures(r"d:\working\monterey\tasking.gdb\MontereyDV", 
                                            "AGL", 
																																												r"d:\working\monterey\results.gdb\obstacles", 
                                            r"d:\working\monterey\results.gdb\buffers", 
                                            r"d:\working\monterey\tasking.gdb\mtyAOI")