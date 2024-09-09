# Forecast temperature using exponential smoothing.

# Import system modules.
import arcpy

# Set property to overwrite existing output.
arcpy.env.overwriteOutput = True

# Set workspace.
workspace = r"C:\Analysis"
arcpy.env.workspace = workspace

# Forecast three time steps.
arcpy.stpm.ExponentialSmoothingForecast("Temperature.nc","Temp_NONE_ZEROS", 
                                        "Analysis.gdb/Forecasts", 
                                        "outForecastCube.nc", 3, 2, 5,
                                        "IDENTIFY", "90%", 4)

# Create a feature class visualizing the forecasts.
arcpy.stpm.VisualizeSpaceTimeCube3D("outForecastCube.nc", "Temp_NONE_ZEROS", 
                                    "VALUE", "Analysis.gdb/ForecastsFC")