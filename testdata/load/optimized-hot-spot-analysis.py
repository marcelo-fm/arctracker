# Analyze the spatial distribution of 911 calls in a metropolitan area

# Import system modules
import arcpy

# Set property to overwrite existing output, by default
arcpy.env.overwriteOutput = True

# Local variables...
workspace = r"C:\OHSA\data.gdb"

try:
    # Set the current workspace (to avoid having to specify the full path to 
    # the feature classes each time)
    arcpy.env.workspace = workspace

    # Create a polygon that defines where incidents are possible  
    # Process: Minimum Bounding Geometry of 911 call data
    arcpy.management.MinimumBoundingGeometry("Calls911", "Calls911_MBG", 
                                             "CONVEX_HULL", "ALL", "#", 
                                             "NO_MBG_FIELDS")

    # Optimized Hot Spot Analysis of 911 call data using fishnet aggregation method with a bounding polygon of 911 call data
    # Process: Optimized Hot Spot Analysis 
    ohsa = arcpy.stats.OptimizedHotSpotAnalysis("Calls911", "Calls911_ohsaFishnet", 
                                                "#", "COUNT_INCIDENTS_WITHIN_FISHNET_POLYGONS", 
                                                "Calls911_MBG") 

except arcpy.ExecuteError:
    # If any error occurred when running the tool, print the messages
    print(arcpy.GetMessages())