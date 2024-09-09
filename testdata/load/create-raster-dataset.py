##==================================
##Create Raster Dataset
##Usage: CreateRasterDataset_management out_path out_name {cellsize} 8_BIT_UNSIGNED | 1_BIT | 2_BIT | 4_BIT | 8_BIT_SIGNED 
##                                      | 16_BIT_UNSIGNED | 16_BIT_SIGNED | 32_BIT_UNSIGNED | 32_BIT_SIGNED | 32_BIT_FLOAT 
##                                      | 64_BIT {raster_spatial_reference} number_of_bands {config_keyword} {pyramids} {tile_size} 
##                                      {compression} {pyramid_origin}

import arcpy
arcpy.env.workspace = r"\\workspace\PrjWorkspace\RasGP"
##Create a empty TIFF format Raster Dataset with the following parameters
##Cellsize: 2
##Pixel type: 8 Bit Unsigned Integer
##Number of Bands: 3
##Pyramid: Build full pyramids with NEAREST interpolation and JPEG compression
##Compression: NONE
##Projection: World_Mercator
##Tile size: 128 128
arcpy.CreateRasterDataset_management("CreateRD","EmptyTIFF.tif","2","8_BIT_UNSIGNED",\
                                     "World_Mercator.prj", "3", "", "PYRAMIDS -1 NEAREST JPEG",\
                                     "128 128", "NONE", "")

##Create a SDE Raster Dataset
##No Spatial Reference, with Pyramid Origin
arcpy.CreateRasterDataset_management("CreateRD\\CreateRD.gdb","NewRD","10","16_BIT_UNSIGNED",\
                                     "", "1", "MAX_FILE_SIZE_4GB", "PYRAMIDS 3 BILINEAR DEFAULT",\
                                     "128 128", "JPEG2000 80", "-20037508.34278775 30198185.16987658")