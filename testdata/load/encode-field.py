# Import system modules.
import arcpy

try:
    # Set the workspace and input features.
    arcpy.env.workspace = r"C:\\Encoded\\MyData.gdb"
    inputFeatures = 'San_Francisco_Crimes'

    # Set input features, dependent variable, and explanatory variable.
    in_table = 'San_Francisco_Crimes'
    field = 'Dates'

    # Set encoding Method
    encoding_method = "TEMPORAL"

    # Set time Step Interval
    time_step_interval = '1 Days'

    # Set Time Step Alignment
    time_step_alignment = "START_TIME"

    # Run Encode Field Tool.
    arcpy.management.EncodeField(in_table, field, encoding_method, 
                    None, time_step_interval, time_step_alignment)

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message.
    print(arcpy.GetMessages())