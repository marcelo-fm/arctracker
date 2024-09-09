# Compare and merge three forecasts

# Import system modules
import arcpy

# Set property to overwrite existing output.
arcpy.env.overwriteOutput = True

# Set workspace
workspace = r"C:\Analysis"
arcpy.env.workspace = workspace

# Run tool
arcpy.stpm.EvaluateForecastsByLocation(["CurveFit.nc", "ExpSmooth.nc", "ForestBased.nc"], 
                                       "Analysis.gdb/Forecasts", "outEvaluate.nc",
                                       "USE_VALIDATION")