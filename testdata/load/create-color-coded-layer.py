import arcpy
arcpy.env.baDataSource = "USA_ESRI_2018"
arcpy.ba.ColorCodedLayer(r"c:\users\<User ID>\documents\arcgis\projects\my_project\bayarea_proprietarydata.sdcx/sales_s01_sales", "sales_s01_sales Layer", "NATURAL_BREAKS", 5)