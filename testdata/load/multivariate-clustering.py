# Clustering Vandalism data in a metropolitan area
# using the Multivariate Clustering Tool

# Import system modules
import arcpy

# Set environment property to overwrite existing output, by default
arcpy.env.overwriteOutput = True

try:
    # Set the current workspace (to avoid having to specify the full path to
    # the feature classes each time)
    arcpy.env.workspace = r"C:\GA"

    # Join the 911 Call Point feature class to the Block Group Polygon feature 
    # class
    # Process: Spatial Join
    fieldMappings = arcpy.FieldMappings()
    fieldMappings.addTable("ReportingDistricts.shp")
    fieldMappings.addTable("Vandalism2006.shp")

    sj = arcpy.SpatialJoin_analysis("ReportingDistricts.shp", 
                                    "Vandalism2006.shp", "Dist_Vand.shp", 
                                    "JOIN_ONE_TO_ONE","KEEP_ALL", fieldMappings, 
                                    "COMPLETELY_CONTAINS")

    # Use the Multivariate Clustering tool to create groups based on different 
    # variables or analysis fields
    # Process: Cluster Similar Features  
    ga = arcpy.MultivariateClustering_stats("District_Vandalism", "outVandalism", 
                                            ["Join_Count", "TOTPOP", "VACANT_CY", "UNEMP"],
	             																														"K_MEANS", "OPTIMIZED_SEED_LOCATIONS", 
                                            None, 5)
    
    # Use Summary Statistic tool to get the Mean of variables used to group
    # Process: Summary Statistics
    SumStat = arcpy.Statistics_analysis("outVandalism", "outSS", 
                                        [["Join_Count", "MEAN"], 
                                         ["VACANT_CY", "MEAN"], 
                                         ["TOTPOP_CY", "MEAN"], 
                                         ["UNEMP_CY", "MEAN"]], 
                                        "GSF_CLUSTER")

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print out the error message.
    print(arcpy.GetMessages())