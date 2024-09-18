##====================================
##Delete Colormap
##Usage: CalculateStatistics_management in_raster
    
import arcpy
arcpy.env.workspace = r"C:/Workspace"

##Delete the colormap of single band image if exist
arcpy.DeleteColormap_management("nocolormap.img")