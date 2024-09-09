import arcpy
import pandas
import os

arcpy.env.overwriteOutput = True

in_table = r"d:\data\states.shp"
out_table = r"in_memory\stats_table"
stat_fields = [['POP1990', 'SUM'], ['POP1997', 'SUM']]

stats = arcpy.analysis.Statistics(in_table, out_table, stat_fields,
                                  case_field='SUB_REGION')

# Get a list of field names to display
field_names = [i.name for i in arcpy.ListFields(out_table) if i.type != 'OID']

# Open a cursor to extract results from stats table
cursor = arcpy.da.SearchCursor(out_table, field_names)

# Create a pandas DataFrame to display results
df = pandas.DataFrame(data=[row for row in cursor],
                      columns=field_names)

print(df)