import arcpy
arcpy.env.workspace = "C:/temp"
arcpy.CreateVoxelSceneLayerContent_management("pm10.lyrx", "voxel.slpk")