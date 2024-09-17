# Import system modules
import arcpy
from arcpy.ia import *

# Set local variables
in_trajectory_dataset = r"C:\temp\trajectory_data.gdb\trajectory_dataset"
paths_list = "* C:\data\CryoSat"
where_clause = "OBJECTID<2"


# Execute
repair_output = arcpy.management.RepairTrajectoryDatasetPaths(in_trajectory_dataset, paths_list, where_clause)