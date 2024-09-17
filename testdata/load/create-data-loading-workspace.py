# Name: CreateDataLoadingWorkspace.py
# Description: Create a new Data Loading Workspace

# Import required modules
import os
import arcpy

# Source and target workspaces with the mapping of table name to table name.
source_workspace = "C:/data/WaterUtilities.gdb/WaterDistribution"
target_workspace = "C:/data/Water_AssetPackage.gdb/UtilityNetwork"
mapping = [
    ("wControlValve", "WaterDevice"),
    ("wHydrant", "WaterJunction"),
    ("wFitting", "WaterJunction"),
    ("wMain", "WaterLine"),
]

# Fully qualify the table names.
source_target = [(os.path.join(source_workspace, a), os.path.join(target_workspace, b)) for a, b in mapping]

# Set local variables.
output_folder = "C:/data"
mapping_table = "C:/temp/Default.gdb/DataReference_GenerateMappingTable"

arcpy.management.CreateDataLoadingWorkspace(
    source_target_mapping=source_target,
    out_folder=output_folder,
    match_options="MATCH_FIELDS;MATCH_VALUES",
    mapping_table=mapping_table,
    calc_stats=True,
    match_subtypes=True,
)