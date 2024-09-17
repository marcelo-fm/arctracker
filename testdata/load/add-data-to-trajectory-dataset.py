# Import system modules
import arcpy
from arcpy.ia import *

# Set local variables
in_trajectory_dataset = r"C:\temp\trajectory_data.gdb\trajectory_dataset"

input_path = r"C:\data\Cryosat\CS_OFFL_SIR_LRM_2__20210301T000738_20210301T001611_D001.nc"

# Execute
trajectory_output = arcpy.management.AddDataToTrajectoryDataset(in_trajectory_dataset, 
		   "Cryosat-2", input_path, "*CS_*.nc", "SUBFOLDERS", None)