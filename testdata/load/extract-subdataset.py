##====================================
##Extract Subdataset
##Usage: ExtractSubdataset_management in_raster out_raster {ID;ID...}

import arcpy
arcpy.env.workspace = r"C:/Workspace"

##Extract 3-band subdataset from HDF
arcpy.ExtractSubDataset_management("MHDF.hdf", "subds.tif", "5;6;7")

##Extract 1-band subdataset from NITF
arcpy.ExtractSubDataset_management("MNITF.ntf","subds_ntf.tif", "2")