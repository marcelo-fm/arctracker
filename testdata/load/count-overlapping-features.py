# CountOverlappingFeatures_Example_2.py
# Description: Count number of cellular service providers for given area

# Import the system modules
import arcpy

# Set current workspace
arcpy.env.workspace = r"C:\data\data.gdb"

# Set input parameters
provider_a = 'Provider_A_ServiceArea'
provider_b = 'Provider_B_ServiceArea'
provider_c = 'Provider_C_ServiceArea'
in_fcs  = [provider_a, provider_b, provider_c]

# Set output feature names
out_fc = 'CellularProviders_Count'
out_tbl = 'CellularProviders_Count_Tbl'

# Obtain overlap count for three overlapping input feature classes
# and use minimum_overlap_count parameter to limit the output to only 
# those areas where all three overlap.
arcpy.analysis.CountOverlappingFeatures(in_fcs, out_fc, 3, out_tbl)