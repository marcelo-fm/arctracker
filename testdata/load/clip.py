##Clip while maintaining original extent



import arcpy

arcpy.env.workspace = "C:/Workspace"



arcpy.Clip_management("c:\\test\\image.tif", "2536996.21761925 7365614.23930381 2537634.12209192 7366302.3861673", 
                      "c:\\output\\clip.tif", "c:\\test\\clipfeature.shp", "0", "ClippingGeometry", 
                      "MAINTAIN_EXTENT")