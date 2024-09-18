# Set the properties of a spatial statistics model file 

# Import modules 
import arcpy 

# Set the current workspace 
arcpy.env.workspace = "C:/MyData" 

# Set Variable Description and units 
var_predict = [["FatalityPresence", "Binary value to show presence of fatality", "No Units"]]
var_exp = [["ALCOHOL_RELATED", "Number of accidents related to alcohol usage", "Count"], 
           ["SPEED", "Speed of the vehicle", "Miles per hour"]]
var_distance = [["INTERSECTION", "Distance to a road intersection", "Miles"]]

# Run tool  
arcpy.stats.SetSSMFileProperties("input_modelfile.ssm", var_predict, var_exp, 
          var_distance) 

# Print geoprocessing messages 
print(arcpy.GetMessages)