# Grouping Analysis of Vandalism data in a metropolitan area
# using the Grouping Analysis Tool

# Import system modules
import arcpy
import os

# Set geoprocessor object property to overwrite existing output, by default
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
                                    "JOIN_ONE_TO_ONE", "KEEP_ALL", 
                                    fieldMappings, "COMPLETELY_CONTAINS")
    
    # Use Grouping Analysis tool to create groups based on different variables 
    # or analysis fields
    # Process: Group Similar Features  
    ga = arcpy.stats.GroupingAnalysis("Dist_Vand.shp", "TARGET_FID", 
                                      "outGSF.shp", "4", 
                                      "Join_Count;TOTPOP_CY;VACANT_CY;UNEMP_CY",
                                      "NO_SPATIAL_CONSRAINT", "EUCLIDEAN", "", 
                                      "", "FIND_SEED_LOCATIONS", "",
                                      "outGSF.pdf", "DO_NOT_EVALUATE")

    # Use Summary Statistic tool to get the Mean of variables used to group
    # Process: Summary Statistics
    SumStat = arcpy.Statistics_analysis("outGSF.shp", "outSS", 
                                        [["Join_Count", "MEAN"], 
                                         ["VACANT_CY", "MEAN"], 
                                         ["TOTPOP_CY", "MEAN"], 
                                         ["UNEMP_CY", "MEAN"]], 
                                        "GSF_GROUP")

except:
    # If an error occurred when running the tool, print out the error message.
    print(arcpy.GetMessages())