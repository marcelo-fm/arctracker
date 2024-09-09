# Estimate the causal effect between fertilizer amount 
# and corn yield using soil type and temperature as
# confounding variables.

# Import required modules.
import arcpy

# Set the workspace.
arcpy.env.workspace = "c:/data/crops.gdb"

# Run Causal Inference Analysis tool with gradient boosting
# and inverse propensity score weighting.
try:
    arcpy.stats.CausalInferenceAnalysis(
        in_features="crop_locations",
        outcome_field="corn_yield",
        exposure_field="fertilizer",
        confounding_variables="soil_type true;temperature false",
        out_features=r"CausalInference_corn_yield",
        ps_method="GRADIENT_BOOSTING",
        balancing_method="WEIGHTING",
        enable_erf_popups="CREATE_POPUP",
        out_erf_table=r"erftable",
        target_outcomes=[],
        target_exposures=[],
        lower_exp_trim=0.01,
        upper_exp_trim=0.99,
        lower_ps_trim=0,
        upper_ps_trim=1,
        num_bins=None,
        scale=None,
        balance_type="MEAN",
        balance_threshold=0.1,
        bw_method="PLUG_IN",
        create_bootstrap_ci="CREATE_CI"
    )

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message.
    print(arcpy.GetMessages())