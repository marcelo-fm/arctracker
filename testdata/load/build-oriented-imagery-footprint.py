import arcpy
arcpy.env.workspace = "C:/data"
arcpy.oi.BuildOrientedImageryFootprint(
    "C:/OrientedImageryExample/MyOI.gdb/MyOrientedImageryDataset", 
    out_dataset_path="C:/OrientedImageryExample/MyOI.gdb",
    out_dataset_name='MyOrientedImageryDataset_footprint',
    footprint_option='MERGE')