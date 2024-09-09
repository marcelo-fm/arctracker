# Import system modules.
import arcpy

try:
    # Set the workspace and input features.
    arcpy.env.workspace = r"C:\\Reclassify\\MyData.gdb"
    in_table = "Demographics"

    # Set the input field that will be reclassified
    field = "Population"

    # Set the reclassification method
    method = "MANUAL"

    # Set the reclassification table
    reclass_table = "10000 Village;100000 Town;1000000 City"

    # Set the output field name
    output_field_name = "SettlementType"

    # Run the Reclassify Field tool
    arcpy.management.ReclassifyField(in_table, field, method, "", 
          None, "", reclass_Table, None, output_field_name)

except arcpy.ExecuteError:
    # If an error occurred when running the tool, print the error message.
    print(arcpy.GetMessages())