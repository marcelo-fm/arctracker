# unions.py
# Purpose: union 3 feature classes

# Import the system modules
import arcpy

# Set the current workspace (to avoid having to specify the full path to the 
# feature classes each time)
arcpy.env.workspace = "c:/data/data.gdb"
 
# Union 3 feature classes but only carry the FID attributes to the output
inFeatures = ["well_buff50", "stream_buff200", "waterbody_buff500"]
outFeatures = "water_buffers"
arcpy.analysis.Union(inFeatures, outFeatures, "ONLY_FID")

# Union 3 other feature classes, but specify some ranks for each 
# since parcels has better spatial accuracy
inFeatures = [["counties", 2], ["parcels", 1], ["state", 2]]
outFeatures = "state_landinfo" 
arcpy.analysis.Union(inFeatures, outFeatures)