#compute block adjustment, case 3

import arcpy
arcpy.env.workspace = "c:/workspace"

#Compute block adjustment specifying an output point table and 
#an setting an adjustment option
mdName = "BD.gdb/redlandsQB"
in_controlPoint = "BD.gdb/redlandsQB_tiePoints"
out_solutionTable = "BD.gdb/redlandsQB_solution"
out_solutionPoint = "BD.gdb/redlandsQB_solutionPoint"
engineOption = "_BAI c:/workspace/bai.txt; _BAO c:/workspace/bao.txt"

arcpy.ComputeBlockAdjustment_rm(mdName, in_controlPoint, 
     "POLYORDER1", out_solutionTable, out_solutionPoint,"0.5", 
     engineOption)