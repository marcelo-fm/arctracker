# Create clusters of store locations with similar sales volumes over time.

# Import system modules.
import arcpy

# Set overwriteOutput property to overwrite existing output, by default.
arcpy.env.overwriteOutput = True

# Set workspace...
workspace = r"C:\Analysis"
arcpy.env.workspace = workspace

# Create 3 clusters of location with similar extent of fluctuation in temperature.
arcpy.stpm.TimeSeriesClustering(r"Temperature.nc", "Air_NONE_ZEROS",
                      r"Analysis.gdb\Temperature_TSC",
                      "PROFILE_FOURIER", 3, "Temp_Chart", None, 
                      "CREATE_POPUP")

# Create a feature class containing all the bins in the input space time cube.
arcpy.stpm.VisualizeSpaceTimeCube3D(r"Temperature.nc", "Air_NONE_ZEROS", "VALUE", 
                      r"Temp_Bins.shp")


# Make the bins as a feature layer.
arcpy.management.MakeFeatureLayer("Temp_Bins.shp", "Temp_Bins_Temp_Layer")

# Join the clustering results to the bins so each bin now has a cluster ID.
arcpy.management.AddJoin("Temp_Bins_Temp_Layer", "Location", 
                      r"Analysis.gdb\Temperature_TSC", "Location", "KEEP_ALL")

# Summarize the bins using Summary Statistics with Cluster ID as a case field
# to get the minimum, maximum, and average temperature for each cluster.
arcpy.analysis.Statistics("Temp_Bins_Temp_Layer", "Temp_Bins_Statistics.shp",
                      "Temp_Bins.VALUE MEAN;Temp_Bins.VALUE MAX;Temp_Bins.VALUE MIN",
                      "Temperature_TSC.CLUSTER_ID")