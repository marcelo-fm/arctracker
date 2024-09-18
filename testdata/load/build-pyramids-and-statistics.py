##====================================
##Build Pyramids and Statistics
##Usage: BuildPyramidsandStatistics_management in_workspace {INCLUDE_SUBDIRECTORIES
##                                                 | NONE} {BUILD_PYRAMIDS | NONE}
##                                                 {CALCULATE_STATISTICS | NONE}
    
try:
    import arcpy
    arcpy.env.workspace = r"C:/Workspace"

    ##Define parameters for build pyramids and calculate statitics in environment setting
    arcpy.env.pyramid = "PYRAMIDS 3 BILINEAR JPEG"
    arcpy.env.rasterStatistics = "STATISTICS 4 6 (0)"
    
    ##Build pyramids and calculate statistics for all raster in a folder
    arcpy.BuildPyramidsandStatistics_management("folder", "INCLUDE_SUBDIRECTORIES",
                                                "BUILD_PYRAMIDS", "CALCULATE_STATISTICS")
    
    ##Build pyramids and calculate statistics for all raster in a GDB
    arcpy.BuildPyramidsandStatistics_management("fgdb.gdb", "INCLUDE_SUBDIRECTORIES",
                                                "BUILD_PYRAMIDS", "CALCULATE_STATISTICS")
    
    ##Build pyramids and calculate statistics for all raster in a Mosaic Dataset
    arcpy.BuildPyramidsandStatistics_management("fgdb.gdb/md", "INCLUDE_SUBDIRECTORIES",
                                                "BUILD_PYRAMIDS", "CALCULATE_STATISTICS")

except:
    print "Build Pyramids and Statistics example failed."
    print arcpy.GetMessages()