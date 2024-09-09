# Create Space Time Cube by aggregating homicide incidents in a metropolitan area

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

    # Create Space Time Cube by aggregating homicide incident data with 3 months and 3 miles settings
    # Process: Create Space Time Cube By Aggregating Points
    cube = arcpy.stpm.CreateSpaceTimeCube("Homicides.shp", "Homicides.nc", "MyDate", "#", 
                                          "3 Months", "End time", "#", "3 Miles", "Property MEDIAN SPACETIME; Age STD ZEROS", "HEXAGON_GRID")

    # Create a polygon that defines where incidents are possible  
    # Process: Minimum Bounding Geometry of homicide incident data
    arcpy.management.MinimumBoundingGeometry("Homicides.shp", "bounding.shp", "CONVEX_HULL",
                                             "ALL", "#", "NO_MBG_FIELDS")

    # Local Outlier Analysis of homicide incident cube using 5 Miles neighborhood 
    # distance and 2 neighborhood time step with 499 permutations to detect outliers
    # Process: Local Outlier Analysis
    loa = arcpy.stpm.LocalOutlierAnalysis("Homicides.nc", "COUNT", "LOA_Homicides.shp", "5 Miles",
                                          2, 499, "bounding.shp", "FIXED_DISTANCE")
except arcpy.ExecuteError:
    # If any error occurred when running the tool, print the messages
    print(arcpy.GetMessages())