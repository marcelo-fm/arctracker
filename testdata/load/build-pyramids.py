#Build Pyramids for multiple raster datasets in the workspace
#Skip the dataset that already has pyramid
#Build pyramids with compression and level setting

import arcpy
arcpy.env.workspace = "C:/Workspace"

    
inras = "image1.tif;image2.img;fgdb.gdb/image3"
pylevels = "6"
skipfirst = "SKIP_FIRST"
resample = "BILINEAR"
compress = "JPEG"
quality = "80"
skipexist = "SKIP_EXISTING"

arcpy.BatchBuildPyramids_management(
     inras, pylevels, skipfirst, resample, compress,
     quality, skipexist)