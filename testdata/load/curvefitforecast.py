# Forecast population levels using curve fitting.

# Import system modules.
import arcpy

# Set property to overwrite existing output.
arcpy.env.overwriteOutput = True

# Set workspace.
workspace = r"C:\Analysis"
arcpy.env.workspace = workspace

# Forecast three time steps using auto-detect.
arcpy.stpm.CurveFitForecast("Population.nc", "Pop_NONE_ZEROS", 
                            "Analysis.gdb/Forecasts", "outForecastCube.nc"
                            3, "AUTO_DETECT", 5, "IDENTIFY", "90%", 4)

# Create a feature class visualizing the forecasts.
# Output can only be viewed in a Scene view.
arcpy.stpm.VisualizeSpaceTimeCube3D("outForecastCube.nc", "Pop_NONE_ZEROS", 
                                    "VALUE", "Analysis.gdb/ForecastsFC")