##===========================
##Import Mosaic Dataset Geometry
##Usage: ImportMosaicDatasetGeometry_management in_mosaic_dataset FOOTPRINT | SEAMLINE
##                                       | BOUNDARY target_join_field 
##                                       input_featureclass input_join_field 

import arcpy
arcpy.env.workspace = "c:/PrjWorkspace/RasGP"

# Import shape file geometry as Mosaic Dataset Footprints
# Note: Feature class FID starts with 0
arcpy.ImportMosaicDatasetGeometry_management("Geometry.gdb/md",
                                            "FOOTPRINT", "OBJECTID",
                                            "infootprint.shp", "FTID")                                      

# Import GDB feature class as Mosaic Dataset Boundary
arcpy.ImportMosaicDatasetGeometry_management("Geometry.gdb/md", "BOUNDARY",
                                      "OBJECTID", "Geometry.gdb/inboundary",
                                      "OBJECTID")