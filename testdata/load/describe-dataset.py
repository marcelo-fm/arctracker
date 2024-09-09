#-------------------------------------------------------------------------------
# Name: DescribeDataset.py
# Description: 

# Import system modules
import arcpy
arcpy.env.workspace = "C:/data/RedRiver_basin.gdb"

# Set local variables
inputDataset = "WaterSample"
output = "WSample_summary"
sample = "WSample_sample2500"

# Run Describe Dataset
arcpy.gapro.DescribeDataset(inputDataset, output, 2500, sample)