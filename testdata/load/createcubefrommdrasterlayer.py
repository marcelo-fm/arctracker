# Convert a multidimensional raster layer to a space-time cube
# Fill in missing values using space-time neighbors
# Run Emerging Hot Spot Analysis on the data
# Visualize the results in 3d

# Import system modules
import arcpy

# Set overwriteOutput property to overwrite existing output by default
arcpy.env.overwriteOutput = True

# Local variables ...
arcpy.env.workspace = r"C:\STPM\CSTCMDRL"

try:

    # Create a space-time cube from the multidimensional raster layer
    arcpy.stpm.CreateSpaceTimeCubeMDRasterLayer(r"Precipitation_MDRLayer",
                                       r"SierraNevada_Precipitation.nc", 
                                       "SPACE_TIME_NEIGHBORS")

    # Run an emerging hot spot analysis on the space-time cube
    # using contiguity edges and corners so that neighbors are defined
    # by all bordering bins in space and time.
    arcpy.stpm.EmergingHotSpotAnalysis(r"SierraNevada_Precipitation.nc",
                                       "PRECIPITATION_SPACE_TIME_NEIGHBORS",
                                       "SierraNevada_Precipitation_EmergingHotSpot", 
                                       "", 1, "", "CONTIGUITY_EDGES_CORNERS")

    # Use Visualize Cube in 3d to see the hot spot results for each time slice
    arcpy.stpm.VisualizeSpaceTimeCube3D(r"SierraNevada_Precipitation.nc", 
                                        "PRECIPITATION_SPACE_TIME_NEIGHBORS",
                                        "HOT_AND_COLD_SPOT_RESULTS",
                                        "SierraNevada_Precipitation_Visualize3d")

except arcpy.ExecuteError:
    # If any error occurred while running the tool, print the messages
    print(arcpy.GetMessages())