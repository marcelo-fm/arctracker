import arcpy

# Set local variables
in_table = "C:/Data/Garbo.gdb/trails"  # Note: empty feature class
field = "condition_rating"  # short int, non nullable field
new_field_name = "notes"
new_field_alias = "Comments on Trail Condition"
field_type = "TEXT"
field_length = 60
field_is_nullable = "NULLABLE"
clear_field_alias = "FALSE"

# Alter the properties of a non nullable, short data type field to become a text field
arcpy.management.AlterField(in_table,
                            field,
                            new_field_name,
                            new_field_alias,
                            field_type,
                            field_length,
                            field_is_nullable,
                            clear_field_alias)