#apply block adjustment
import arcpy
arcpy.env.workspace = "c:/workspace"

#Apply the block ajustment
mdName = "BD.gdb/redlandsQB"
out_solutionTable = "BD.gdb/redlandsQB_solution"

arcpy.ApplyBlockAdjustment_rm(mdName, "ADJUST", 
     out_solutionTable, 0.25)