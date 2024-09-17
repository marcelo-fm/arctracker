# Compare hot spot analysis results for robberies and social disorder.

# Import required modules.
import arcpy

# Set the workspace.
arcpy.env.workspace = "c:/data/boston.gdb"

# Create hot spot result for robberies in Boston.
robbery_hs = arcpy.stats.HotSpots(
    "boston_ecometrics_hex", "robbery", "robbery_hotspot",
     "K_NEAREST_NEIGHBORS", None, None, None, None, None, None, 8
)

# Create hot spot result of social disorder in Boston.
social_disorder_hs = arcpy.stats.HotSpots(
    "boston_ecometrics_hex", "scl_dsr", "social_disorder_hotspot", 
    "K_NEAREST_NEIGHBORS", None, None, None, None, None, None, 8
)

# Compare robbery and social disorder hot spot results.
try:
    hs_compare = arcpy.stats.HotSpotAnalysisComparison(
        robbery_hs, social_disorder_hs, "robbery_disorder_comparison", 8, 999, "FUZZY", 
        None, None, False
    )
except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message.
    print(arcpy.GetMessages())

# Save similarity and kappa derived outputs.
result_vals = [hs_compare.getOutput(out) for out in range(hs_compare.outputCount)]

# Apply labels to derived outputs
results_names = ["output_fc", "similarity", "expected_similarity", "fuzzy_kappa", 
    "output_layer"]

# Combine to dictionary and print derived outputs.
results = dict(zip(results_names, result_vals))
results