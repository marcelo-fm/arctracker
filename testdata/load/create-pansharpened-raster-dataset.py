#3 Band RGB Pansharpen with Brovey algorithm

import arcpy
arcpy.env.workspace = "C:/workspace"
    
arcpy.CreatePansharpenedRasterDataset_management(
     "rgb.img","3","2","1","1", "output\\rgb_pan.img","pan.img","Brovey")