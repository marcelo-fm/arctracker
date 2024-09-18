# imports
import arcpy

# output from Convert Coordinate Notation tool
# for DD_2 (and also for DD_1) format, the output values are in string format
# for example, for DD_1, the output values may be '43.63872N 116.24135W'
in_table = r"c:\data\ccn.gdb\ccn_dd1"

# add a field of type DOUBLE to store the numeric longitude value
arcpy.AddField_management(in_table, "DDLonDbl", "DOUBLE")

# now call CalculateField tool to convert the values, 'W' is negative
expr = """def convertToDouble(fldval):
    val = float(fldval[:-1])
    if fldval[-1:] == 'W':
        return val * -1.0
    else:
        return val"""

# DDLon field contains longitudes in a string field
arcpy.CalculateField_management(in_table,"DDLonDbl","convertToDouble(!DDLon!)","PYTHON_9.3",expr)
    
# add another field to store the numeric longitude value
arcpy.AddField_management(in_table, "DDLatDbl", "DOUBLE")

# call CalculateField again to convert the values, 'S' is negative
expr = """def convertToDouble(fldval):
    val = float(fldval[:-1])
    if fldval[-1:] == 'S':
        return val * -1.0
    else:
        return val"""

# DDLat field contains latitudes in a string field
arcpy.CalculateField_management(in_table,"DDLatDbl","convertToDouble(!DDLat!)","PYTHON_9.3",expr)