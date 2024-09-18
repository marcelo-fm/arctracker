# Create Referenced Mosaic Dataset from existing Mosaic Dataset
# Use shape file to clip the source mosaic dataset


import arcpy
arcpy.env.workspace = "C:/Workspace"

arcpy.CreateReferencedMosaicDataset_management(
     "RefMD.gdb/md", "ref_md.amd", "GCS_WGS_1984.prj", "1", "#", "#", 
     "ref_md.shp", "#", "SELECT_USING_FEATURES", "#", "#", "#", "#", 
     "NO_BOUNDARY")