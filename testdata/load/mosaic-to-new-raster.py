##==================================
##Mosaic To New Raster
##Usage: MosaicToNewRaster_management inputs;inputs... output_location raster_dataset_name_with_extension 
##                                    {coordinate_system_for_the_raster} 8_BIT_UNSIGNED | 1_BIT | 2_BIT | 4_BIT 
##                                    | 8_BIT_SIGNED | 16_BIT_UNSIGNED | 16_BIT_SIGNED | 32_BIT_FLOAT | 32_BIT_UNSIGNED 
##                                    | 32_BIT_SIGNED | | 64_BIT {cellsize} number_of_bands {LAST | FIRST | BLEND  | MEAN 
##                                    | MINIMUM | MAXIMUM} {FIRST | REJECT | LAST | MATCH}                               

import arcpy
arcpy.env.workspace = r"\\MyMachine\PrjWorkspace\RasGP"

##Mosaic several TIFF images to a new TIFF image
arcpy.MosaicToNewRaster_management("landsatb4a.tif;landsatb4b.tif","Mosaic2New", "landsat.tif", "World_Mercator.prj",\
                                   "8_BIT_UNSIGNED", "40", "1", "LAST","FIRST")