# Import system modules. 
import arcpy 
 
try: 
    # Set the workspace and input features. 
    arcpy.env.workspace = r"C:\\Transform\\MyData.gdb" 
    inputFeatures = "County_Data" 
 
    # Set the input fields that will be standardized. 
    fields = "population_total;unemployment_rate;income" 
 
    # Set the standardization method. 
    method = "BOX-COX" 
 
    # Run the Transform Field tool. 
    arcpy.management.TransformField(inputFeatures, fields, method) 
 
except arcpy.ExecuteError: 
    # If an error occurred when running the tool, print the error message. 
    print(arcpy.GetMessages())