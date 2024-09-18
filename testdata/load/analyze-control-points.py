#analyze control points
import arcpy
arcpy.env.workspace = "c:/workspace"

#analyze the control points using a mask
mdName = "BD.gdb/redlandsQB"
in_controlPoint = "BD.gdb/redlandsQB_tiePoints"
out_coverage = "BD.gdb/out_overage"
out_overlap = "BD.gdb/out_overlap"
in_mask = "BD.gdb/mask"

arcpy.AnalyzeControlPoints_rm(mdName, in_controlPoint, 
     out_coverage, out_overlap, in_mask, 5)