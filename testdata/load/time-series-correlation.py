# Estimate the time lag between infection and 
# hospitalization for seasonal influenza.

# Import required modules.
import arcpy

# Set the workspace.
arcpy.env.workspace = "c:/data/data.gdb"

# Run Time Series Cross Correlation
# Use neighbors and calculate p-values
try:
    arcpy.stats.CausalInferenceAnalysis(
        in_cube=r"c:\data\FluData.nc",
        analysis_variable_1="FLU_CASES",
        analysis_variable_2="HOSPITALIZATIONS",
        output_features=r"CrossCorrResults",
        enable_pop_ups="POPUP",
        max_lag=10,
        lag_direction="BOTH",
        neighborhood_type="K_NEAREST_NEIGHBORS",
        num_nbrs=8,
        distance_band=None,
        spatial_weights="BISQUARE",
        filter_option="FILTER",
        out_corr_table=r"LagCorrTable",
        out_pair_table=r"PairCorrTable"
    )
except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message.
    print(arcpy.GetMessages())