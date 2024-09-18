import arcpy
arcpy.env.workspace = "C:/data"
arcpy.oi.AddImagesToOrientedImageryDataset(
    "C:/OrientedImageryExample/MyOI.gdb/MyOrientedImageryDataset", 
    imagery_category="Oblique",
    input_data='C:/OrientedImageryExample/Samples/img1.jpg;C:/OrientedImageryExample/Samples/img2.jpg')