# Create Space Time Cube of homicide incidents in a metropolitan area

# Import system modules
import arcpy

# Set overwriteOutput property to overwrite existing output, by default
arcpy.env.overwriteOutput = True

# Local variables...
workspace = r"C:\STPM"

try:
    # Set the current workspace (to avoid having to specify the full path to the feature 
    # classes each time)
    arcpy.env.workspace = workspace

    # Create Space Time Cube of homicide incident data with 3 months and 3 miles settings
    # Process: Create Space Time Cube 
    cube = arcpy.stpm.CreateSpaceTimeCube("Homicides.shp", "Homicides.nc", "MyDate", "#", 
                                          "3 Months", "End time", "#", "3 Miles", "Property MEDIAN SPACETIME; Age STD ZEROS",
																																										"HEXAGON_GRID")

    # Create a polygon that defines where incidents are possible  
    # Process: Minimum Bounding Geometry of homicide incident data
    arcpy.management.MinimumBoundingGeometry("Homicides.shp", "bounding.shp", "CONVEX_HULL",
                                             "ALL", "#", "NO_MBG_FIELDS")

    # Emerging Hot Spot Analysis of homicide incident cube using 5 Miles neighborhood 
    # distance and 2 neighborhood time step to detect hot spots
    # Process: Emerging Hot Spot Analysis 
    cube = arcpy.stpm.EmergingHotSpotAnalysis("Homicides.nc", "COUNT", "EHS_Homicides.shp", 
                                              "5 Miles", 2, "bounding.shp", "FIXED_DISTANCE", "3")

except arcpy.ExecuteError:
    # If any error occurred when running the tool, print the messages
    print(arcpy.GetMessages())