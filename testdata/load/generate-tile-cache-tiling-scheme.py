#Generate tiling scheme for a mosaic dataset
#Generate 5 default scales



import arcpy
arcpy.env.workspace = "C:/Workspace"

mdname = "C:/Workspace/Cache.gdb/md"
outScheme = "C:/Workspace/Schemes/Tilingscheme.xml"
method = "NEW"
numscales = "5"
predefScheme = "#"
scales = "#"
scaleType = "SCALE"
tileOrigin = "-20037700 30198300"
dpi = "96"
tileSize ="256 x 256"
tileFormat = "MIXED"
compQuality = "75"
storageFormat = "COMPACT"

arcpy.GenerateTileCacheTilingScheme_management(
     mdName, outScheme, method, numscales, predefScheme, scales,
     scaleType, tileOrigin, dpi, tileSize, compQuality, storageFormat)