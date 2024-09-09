# Linear regression using a count model to predict the number of crimes.
# The depend variable (total number of crimes) is predicted using total
# population, the median age of housing, and average household income.
 
import arcpy

# Set the current workspace (to avoid having to specify the full path to
# the feature classes each time)

arcpy.env.workspace = r"c:\data\project_data.gdb"

arcpy.stats.GWR("crime_counts", "total crimes", "COUNT", "YRBLT;TOTPOP;AVGHINC", 
     "out_features", "NUMBER_OF_NEIGHBORS", "GOLDEN_SEARCH", 30, None, None, None, 
     None, None, None, None, None, "prediction_locations", 
     "YRBLT YRBLT;TOTPOP TOTPOP;AVGHINC AVGHINC", "predicted_counts", 
     "NON_ROBUST", "BISQUARE", r"c:\data\out_rasters")