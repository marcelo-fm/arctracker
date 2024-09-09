import arcpy
arcpy.env.workspace = 'C:/data'
arcpy.ddd.BuildLasDatasetPyramid('test.lasd', 'MIN_Z')