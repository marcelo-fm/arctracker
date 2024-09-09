# Use the output from the Describe Space Time Cube tool to 
# test whether a set of space-time cubes match a set of criteria. Input the 
# space-time cubes that pass the criteria to the Evaluate Forecast by Location 
# tool.

# Import system modules
import os
import glob
import arcpy

# Set Workspace
arcpy.env.workspace = r"C:\Describe"
out_gdb = os.path.join(arcpy.env.workspace, "GDB.gdb")
arcpy.env.overwriteOutput = True

# Assign global variables
check_fields = ['MIN_X', 'MIN_Y', 'MAX_X', 'MAX_Y', 'NUM_FORECAST', 
          'FIRST_FORECAST_START', 'FIRST_FORECAST_END',
          'LAST_FORECAST_START','LAST_FORECAST_END', 'VALIDATION_TIME_STEPS']

# Iterate through all the space-time cubes in a folder
evaluate_cubes = ''

for cube in glob.glob(os.path.join(arcpy.env.workspace, '*.nc')):
    cube_suffix = os.path.basename(cube)
    cube_name = os.path.splitext(cube_suffix)[0]

    out_describe_fc_name = ("describe" + "_{}").format(cube_name)
    out_table = os.path.join(out_gdb, out_describe_fc_name)
    
    # Run the Describe Space Time Cube tool and save a characteristics table into a GDB
    arcpy.stpm.DescribeSpaceTimeCube(cube, out_table, None)
    lstFields = arcpy.ListFields(out_table)

    for field in lstFields:
        # Check if the space-time cube is a forecast cube
        if field.name == "NUM_FORECAST":     
            with arcpy.da.SearchCursor(out_table, check_fields) as cursor:       
                # Check if the extent, start forecast, end forecast, and validation steps  
                # are all the same
                for row in cursor:
                    if str(row[0]) == '-13847325.1116' and str(row[1]) == '3833847.5631' and \
                       str(row[2]) == '-12704362.5439' and str(row[3]) == '5161307.7693' and \
                       str(row[4]) == '14' and str(row[5]) == '2022-02-27 00:00:02' and \
                       str(row[6]) == '2022-02-28 00:00:01' and str(row[7]) == '2022-03-12 00:00:01' and \
                       str(row[8]) == '2022-03-13 00:00:01' and str(row[9]) == '14':
               
                        # Add the space-time cubes that match the criteria to a string 
                        # that will be input into the Evaluate Forecast by Location tool
                        evaluate_cubes += cube + ';'


# Run the Evaluate Forecast by Location tool
evaluate_output = os.path.join(out_gdb, "Evaluate_Covid19_Forecasts")

arcpy.stpm.EvaluateForecastsByLocation(evaluate_cubes.replace('\\', '/'), evaluate_output, None, "USE_VALIDATION")