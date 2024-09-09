# Detect changes in air temperature.

# Import system modules.
import arcpy

# Set property to overwrite existing output.
arcpy.env.overwriteOutput = True

# Set workspace.
workspace = r"C:\Analysis"
arcpy.env.workspace = workspace

# Detect the largest mean shift of temperature measurements.
arcpy.stpm.ChangePointDetection("Air_Temp.nc", "MAX_DEGREES_F", 
                            "Analysis.gdb/Temperature_Change_Points", 
                            "MEAN", "DEFINED_NUMBER", 1, "", 3)

# Create a feature class visualizing the change point results in a 3D scene view.
arcpy.stpm.VisualizeSpaceTimeCube3D("Air_Temp.nc", "Pop_NONE_ZEROS", 
                                    "VALUE", "Analysis.gdb/ForecastsFC")