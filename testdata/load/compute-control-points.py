#compute control points

import arcpy
arcpy.env.workspace = "c:/workspace"

#compute control points using a mask 
mdName = "BD.gdb/redlandsQB"
in_mask = "BD.gdb/redlandsQB_mask"
out_controlPoint = "BD.gdb/redlandsQB_tiePoints"
out_imageFeature = "BD.gdb/redlandsQB_imageFeatures"

arcpy.ComputeControlPoints_rm(mdName, out_controlPoint, 
     "HIGH", in_mask, out_imageFeature)