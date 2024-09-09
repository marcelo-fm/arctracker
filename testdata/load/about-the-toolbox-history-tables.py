# Positional arguments - skipping optional arguments using empty strings is dependent on 
# the order of the optional parameters
arcpy.management.AddField("schools", "school_id", "LONG", "", "", "", "", "NON_NULLABLE")

# Keyword arguments - position doesn't matter
arcpy.management.AddField("schools", "school_id", "LONG", field_is_nullable="NON_NULLABLE")