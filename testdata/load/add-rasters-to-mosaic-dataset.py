#Add Raster Dataset type Raster to FGDB Mosaic Dataset
#Calculate Cell Size Ranges and Build Boundary
#Build Overviews for Mosaic Dataset upon the 3rd level Raster Dataset pyramid
#Apply TIFF file filter
#Build Pyramids for the source datasets

import arcpy
arcpy.env.workspace = "C:/Workspace"

    
mdname = "AddMD.gdb/md_rasds"
rastype = "Raster Dataset"
inpath = "c:/data/rasds"
updatecs = "UPDATE_CELL_SIZES"
updatebnd = "UPDATE_BOUNDARY"
updateovr = "UPDATE_OVERVIEWS"
maxlevel = "2"
maxcs = "#"
maxdim = "#"
spatialref = "#"
inputdatafilter = "*.tif"
subfolder = "NO_SUBFOLDERS"
duplicate = "EXCLUDE_DUPLICATES"
buildpy = "BUILD_PYRAMIDS"
calcstats = "CALCULATE_STATISTICS"
buildthumb = "NO_THUMBNAILS"
comments = "Add Raster Datasets"
forcesr = "#"
estimatestats = "ESTIMATE_STATISTICS"
auxilaryinput = ""
enablepixcache = "USE_PIXEL_CACHE"
cachelocation = "c:\\test\\cachelocation"

arcpy.management.AddRastersToMosaicDataset(
     mdname,  rastype, inpath, updatecs, updatebnd, updateovr,
     maxlevel, maxcs, maxdim, spatialref, inputdatafilter,
     subfolder, duplicate, buildpy, calcstats, 
     buildthumb, comments, forcesr, estimatestats,
     auxilaryinput, enablepixcache, cachelocation)