# Display Space Time Cube of homicide incidents in a metropolitan area

# Import system modules
import arcpy

# Set environment property to overwrite existing output, by default
arcpy.env.overwriteOutput = True

# Local variables...
workspace = r"C:\STPM"

# Set the current workspace (to avoid having to specify the full path to the 
# feature classes each time)
arcpy.env.workspace = workspace

# Display Space Time Cube of homicide with the standard deviation of victim's 
# age, fill no-data as 0
# Only display the locations excluded from analysis.
# Process: Visualize Space Time Cube in 2D 
cube = arcpy.stpm.VisualizeSpaceTimeCube2D("Homicides.nc", "AGE_STD_ZEROS", 
                                           "LOCATIONS_EXCLUDED_FROM_ANALYSIS", 
                                           "Homicides_Age_LocExc.shp")