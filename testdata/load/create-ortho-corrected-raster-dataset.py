##====================================
##Create Ortho Corrected Raster Dataset
##Usage: CreateOrthoCorrectedRasterDataset_management in_raster out_raster_dataset
##                                                    CONSTANT_ELEVATION | DEM constant_ elevation
##                                                    in_DEM_raster {ZFactor} {ZOffset} {NONE | GEOID}

import arcpy
arcpy.env.workspace = "C:/Workspace"

##Ortho correct with Constant elevation
arcpy.CreateOrthoCorrectedRasterDataset_management("ortho.img", "orthoready.tif",\
                                                   "CONSTANT_ELEVATION", "30", "#",\
                                                   "#", "#", "#")

##Ortho correct with DEM image and Z factors
arcpy.CreateOrthoCorrectedRasterDataset_management("ortho.img", "orthoready_dem.tif",\
                                                   "DEM", "#", "dem.img", "#", "10", "GEOID")