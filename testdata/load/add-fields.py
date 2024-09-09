import arcpy
arcpy.env.workspace = "C:/data/district.gdb"
arcpy.management.AddFields(
    'school', 
    [['school_name', 'TEXT', 'Name', 255, 'Hello world', ''], 
     ['street_number', 'LONG', 'Street Number', None, 35, 'StreetNumDomain'],
     ['year_start', 'DATE', 'Year Start', None, '2017-08-09 16:05:07', '']])