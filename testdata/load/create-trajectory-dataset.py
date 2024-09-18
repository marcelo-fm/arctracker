# Import system modules
import arcpy
from arcpy.ia import *

# Set local variables
in_workspace = r"C:\temp\trajectory_data.gdb"
in_dataset_name = "trajectory_dataset"
coordinate_system = "GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],
					PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]"

# Execute
Trajectory_output = arcpy.CreateTrajectoryDataset_management(in_workspace, in_dataset_name, coordinate_system)