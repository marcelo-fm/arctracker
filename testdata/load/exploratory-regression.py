# Exploratory Regression of 911 calls in a metropolitan area
# using the Exploratory Regression Tool

# Import system modules
import arcpy

# Set property to overwrite existing output, by default
arcpy.env.overwriteOutput = True

try:
    # Set the current workspace (to avoid having to specify the full path to
    # the feature classes each time)
    arcpy.env.workspace = r"C:\ER"

    # Join the 911 Call Point feature class to the Block Group Polygon feature class
    # Process: Spatial Join
    fieldMappings = arcpy.FieldMappings()
    fieldMappings.addTable("BlockGroups.shp")
    fieldMappings.addTable("911Calls.shp")

    sj = arcpy.SpatialJoin_analysis("BlockGroups.shp", "911Calls.shp", "BG_911Calls.shp",
                               "JOIN_ONE_TO_ONE",
                               "KEEP_ALL",
                               fieldMappings,
                               "COMPLETELY_CONTAINS", "", "")

    # Delete extra fieldsto clean up the data
    # Process: Delete Field 
    arcpy.DeleteField_management("BG_911Calls.shp", "OBJECTID;INC_NO;DATE_;MONTH_;STIME; \
                                 SD_T;DISP_REC;NFPA_TYP;CALL_TYPE;RESP_COD;NFPA_SF; \
                                 SIT_FND;FMZ_Q;FMZ;RD;JURIS;COMPANY;COMP_COD;RESP_YN; \
                                 DISP_DT;DAY_;D1_N2;RESP_DT;ARR_DT;TURNOUT;TRAVEL; \
                                 RESP_INT;ADDRESS_ID;CITY;CO;AV_STATUS;AV_SCORE; \
                                 AV_SIDE;Season;DayNight")

    # Create Spatial Weights Matrix for Calculations
    # Process: Generate Spatial Weights Matrix
    swm = arcpy.GenerateSpatialWeightsMatrix_stats("BG_911Calls.shp", "TARGET_FID", "BG_911Calls.swm",
                                             "CONTIGUITY_EDGES_CORNERS",
                                             "EUCLIDEAN", "1", "", "", "ROW_STANDARDIZATION", "", "", "", "")

    # Exploratory Regression Analysis for 911 Calls
    # Process: Exploratory Regression
    er = arcpy.ExploratoryRegression_stats("BG_911Calls.shp",
                                      "Calls",
                                      "Pop;Jobs;LowEduc;Dst2UrbCen;Renters;Unemployed;Businesses;NotInLF; \
                                ForgnBorn;AlcoholX;PopDensity;MedIncome;CollGrads;PerCollGrd; \
                                PopFY;JobsFY;LowEducFY",
                                      "BG_911Calls.swm", "BG_911Calls.txt", "",
                                      "MAX_NUMBER_ONLY", "5", "1", "0.5", "0.05", "7.5", "0.1", "0.1")
 
except:
    # If an error occurred when running the tool, print out the error message.
    print(arcpy.GetMessages())