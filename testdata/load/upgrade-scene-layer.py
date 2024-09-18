import arcpy
arcpy.management.UpgradeSceneLayer(r"C:\temp\buildings.slpk, r"C:\packages", 
                                   "buildings_upgraded",  
                                   r"C:\temp\extracted\out.json", "NONE")