# Import system modules
import arcpy  

# Define input parameters
in_mosaic_dataset= r"C:\CDM_RM.gdb\YVWD"
control_point_table=r"C:\CDM_RM.gdb\YVWD_ControlPoints"
solution_point_table= r"C:\CDM_RM.gdb\YVWD_SolutionPoints",
where_clause= "OBJECTID > 2",
skip_existing="SKIP_EXISTING",
adjust_footprints="ADJUST_FOOTPRINTS"

# Execute
arcpy.rm.ComputeDepthMap(in_mosaic_dataset, control_point_table, solution_point_table, where_clause, skip_existing, adjust_footprints)