import arcpy
arcpy.env.workspace = "C:/data"
arcpy.analysis.GraphicBuffer("roads", "C:/output/majorrdsBuffered", "100 Feet", 
                             "SQUARE", "MITER")