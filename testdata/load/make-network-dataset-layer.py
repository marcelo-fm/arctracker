networkDataset = "C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
arcpy.na.MakeNetworkDatasetLayer(networkDataset, draw_elements=["EDGES","TURNS"])