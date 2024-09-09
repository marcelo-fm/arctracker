# Display Space Time Cube of homicide incidents in a metropolitan area

# Import system modules
import arcpy

# Set geoprocessor object property to overwrite existing output, by default
arcpy.env.overwriteOutput = True

# Local variables...
workspace = r"C:\STPM"

arcpy.env.workspace = workspace

# Display Space Time Cube of homicide with the hot and cold spots with crime 
# counts.
# Process: Visualize Space Time Cube in 3D 
cube = arcpy.VisualizeSpaceTimeCube3D_stpm("Homicides.nc", "COUNT", 
                                           "HOT_AND_COLD_SPOT_RESULTS", 
                                           "Homicides_Count_HS.shp")