## Generate raster from Band Arithmetic raster function where method is set to SAVI.

arcpy.management.GenerateRasterFromRasterFunction(
	r"C:\Projects\SAVI.rft.xml", r"C:\Projects\Portland_SAVI.tif", 
	r"Raster C:\Projects\PortlandIKONOS.tif;Method SAVI;'Band Indexes' '4 3 0.33'", 
	None, "TIFF", "CURRENT_SLICE")