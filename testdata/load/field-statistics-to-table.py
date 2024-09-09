# Import system modules.
import arcpy

try:
    # Set the workspace and input features. 
    arcpy.env.workspace = r"C:\\Statistics\\MyData.gdb" 
    in_table = "County_Data" 
 
    # Set the input fields that will be used to calculate statistics. 
    in_fields = "population_total;unemployment_rate;income;county_name;sample_date" 
 
    # Set the output location.
    out_location = r"C:\\Statistics\\MyData.gdb"

    # Set the output table field type and name.
    out_tables = "ALL AllStats_Table;DATE DateStats_Table;NUMERIC NumStats_Table;TEXT TextStats_Table"
 
    # Run the Field Statistics To Table tool 
    arcpy.management.FieldStatisticsToTable (in_table, in_fields, out_location, out_tables) 
 
except arcpy.ExecuteError: 
    # If an error occurred when running the tool, print the error message. 
    print(arcpy.GetMessages())