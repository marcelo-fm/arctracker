# Hot Spot Analysis of 911 calls in a metropolitan area
# using the Incremental Spatial Autocorrelation and Hot Spot Analysis Tools

# Import system modules
import arcpy

# Set property to overwrite existing output, by default
arcpy.env.overwriteOutput = True

# Local variables
workspace = r"C:\ISA"

try:
    # Set the current workspace (to avoid having to specify the full path to 
    # the feature classes each time)
    arcpy.env.workspace = workspace

    # Copy the input feature class and integrate the points to snap together at 
    # 30 feet
    # Process: Copy Features and Integrate
    cf = arcpy.management.CopyFeatures("911Calls.shp", "911Copied.shp")
    integrate = arcpy.management.Integrate("911Copied.shp #", "30 Feet")

    # Use Collect Events to count the number of calls at each location
    # Process: Collect Events
    ce = arcpy.stats.CollectEvents("911Copied.shp", "911Count.shp")

    # Use Incremental Spatial Autocorrelation to get the peak distance
    # Process: Incremental Spatial Autocorrelation
    isa = arcpy.stats.IncrementalSpatialAutocorrelation(ce, "ICOUNT", "20", "", 
                     "", "EUCLIDEAN", "ROW_STANDARDIZATION", "outTable.dbf", 
                     "outReport.pdf")

    # Hot Spot Analysis of 911 Calls
    # Process: Hot Spot Analysis (Getis-Ord Gi*)
    distance = isa.getOutput(2)
    hs = arcpy.stats.HotSpots(ce, "ICOUNT", "911HotSpots.shp", "Fixed Distance Band",
                     "Euclidean Distance", "None",  distance, "", "")

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print out the error message.
    print(arcpy.GetMessages())