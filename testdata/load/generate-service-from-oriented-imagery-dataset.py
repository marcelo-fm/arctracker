import arcpy
arcpy.env.workspace = "C:/data"
arcpy.oi.GenerateServiceFromOrientedImageryDataset(
    "C:/OrientedImageryExample/MyOI.gdb/MyOrientedImageryDataset", 
    service_name="oi_service",
    portal_folder="Test",
    share_with="PRIVATE",
    add_footprint="FOOTPRINT",
    attach_images="ATTACH")