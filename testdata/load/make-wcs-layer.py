##====================================
##Make WCS Layer
##Usage: MakeWCSLayer_management in_wcs_coverage out_wcs_layer {template} {ID;ID...}
    
import arcpy

arcpy.env.workspace = r"C:/Workspace"
input1 = r"GIS Servers\File_TIFF_Amberg on server3\090160_1"
input2 = "http://server3/arcgis/services/File_TIFF_Amberg/ImageServer/WCSServer"

##Create WCS layer from WCS connection file
arcpy.MakeWCSLayer_management(input1, "wcslayer1", "11.844983 49.445367 11.858321 49.453887",
                              "1;2;3")

##Create WCS layer from URL with clipping feature
arcpy.MakeWCSLayer_management(input2, "wcslayer2", "clip.shp", "1;2;3")