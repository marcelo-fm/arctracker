# Import system modules
import arcpy
from arcpy import *

# Set local variables
in_trajectory_file = r"C:\data\Cryosat\CS_OFFL_SIR_LRM_2__20210301T000738_20210301T001611_D001.nc"
out_trajectory_layer = r"C:\data\Cryosat\trajectory_layer
dimension = "CS_OFFL_SIR_LRM_2__20210301T000738_20210301T001611_D001_time_20_ku"
predefined_variables = "SSH;H_SEA_ICE"
variables = "height_1_20_ku"

# Execute
trajectory_output = arcpy.management.MakeTrajectoryLayer(in_trajectory_file, out_trajectory_layer, 
		    	dimension, predefined_variables, variables)