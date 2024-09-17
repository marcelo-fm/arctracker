##====================================
##Add Colormap
##Usage: AddColormap_management in_raster {in_template_raster} {input_CLR_file}

import arcpy
arcpy.env.workspace = r"C:/Workspace"

##Assign colormap using template image
arcpy.AddColormap_management("nocolormap.img", "colormap.tif")

##Assign colormap using clr file
arcpy.AddColormap_management("nocolormap.img", "", "colormap_file.clr")