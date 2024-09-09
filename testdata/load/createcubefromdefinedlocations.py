# Fill missing values using a feature set and related table
# Use the results to create a space-time cube from defined locations
# Run Emerging Hot Spot Analysis on the data
# Visualize the results in 3d

# Import system modules
import arcpy

# Set overwriteOutput property to overwrite existing output, by default
arcpy.env.overwriteOutput = True

# Local variables ...
arcpy.env.workspace = r"C:\STPM\Chicago.gdb"

try:

    # Fill missing values in a feature class containing block group polygon shapes and a related table containing the incidents
    # Since some of the values are missing, fill them using the temporal trend method

    arcpy.stpm.FillMissingValues("Chicago_Feature", "Chicago_FilledFeature", "COUNT", "TEMPORAL_TREND", "", "", NoneNone,
                                 "TIME", "", "MYID", "Chicago_Table", "MYID", "", "", "", "Chicago_FilledTable")



    # Create a defined location space-time cube using a related table
    # Using a reference time at the start of the month to force binning fall on month breaks
    # Using temporal aggregation to sum multiple entries into one month
    # Using the method drop location if missing values since you already filled using Fill Missing Values
    arcpy.stpm.CreateSpaceTimeCubeDefinedLocations("Chicago_FilledFeature", r"C:\STPM\Chicago_Cube.nc", "MYID",
                                                   "APPLY_TEMPORAL_AGGREGATION", "TIME", "1 Months", "REFERENCE_TIME",
                                                   "10/1/2015", "", "COUNT SUM DROP_LOCATIONS", "Chicago_FilledTable",
                                                   "MYID")

    # Run an emerging hot spot analysis on the defined locations cube
    # Using contiguity edges so only block groups that bound each other are considered neighbors
    arcpy.stpm.EmergingHotSpotAnalysis(r"C:\STPM\Chicago_Cube.nc", "COUNT_SUM_NONE",
                                       "Chicago_Cube_EmergingHotSpot", "", 1, "",
                                       "CONTIGUITY_EDGES_ONLY")

    # Use Visualize Cube in 3d to see the hot spot results for each time slice
    arcpy.stpm.VisualizeSpaceTimeCube3D(r"C:\STPM\Chicago_Cube.nc", "COUNT_SUM_NONE", "HOT_AND_COLD_SPOT_RESULTS",
                                        "Chicago_Cube_Visualize3d")

except arcpy.ExecuteError:
    # If any error occurred when running the tool, print the messages
    print(arcpy.GetMessages())