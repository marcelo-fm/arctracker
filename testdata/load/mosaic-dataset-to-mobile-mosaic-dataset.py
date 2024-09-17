import arcpy

arcpy.MosaicDatasetToMobileMosaicDataset_management( 
	“c:/someproject/md/fgdb.gdb/somemd”,
	“c:/someproject/runtime/somesql.geodatabase”, 
	“somemd”, “ProductName == ‘Landsat8’”, 
	“c:/someproject/aoi/somefc.shp”,
	“c:/someproject/runtime/data”, 
	“ALWAYS”, “TIFF”, “JPEG”, “75”)