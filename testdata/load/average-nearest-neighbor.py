# Analyze crime data to determine if spatial patterns are statistically significant
 
# Import system modules
import arcpy
 
# Local variables...
workspace = "C:/data"
crime_data = "burglaries.shp"

try:
    # Set the current workspace (to avoid having to specify the full path to the 
    # feature classes each time)
    arcpy.env.workspace = workspace
 
    # Obtain Nearest Neighbor Ratio and z-score
    # Process: Average Nearest Neighbor...
    nn_output = arcpy.stats.AverageNearestNeighbor(crime_data, "EUCLIDEAN_DISTANCE", 
                                                   "NO_REPORT")
    
    # Create list of Average Nearest Neighbor output values by splitting the 
    # result object
    print("The nearest neighbor index is: " + nn_output[0])
    print("The z-score of the nearest neighbor index is: " + nn_output[1])
    print("The p-value of the nearest neighbor index is: " + nn_output[2])
    print("The expected mean distance is: " + nn_output[3])
    print("The observed mean distance is: " + nn_output[4])
    print("The path of the HTML report: " + nn_output[5])
 
except arcpy.ExecuteError:
    # If an error occurred when running the tool, print out the error message.
    print(arcpy.GetMessages())