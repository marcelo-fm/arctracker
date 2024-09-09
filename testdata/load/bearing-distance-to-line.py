# Import system modules
import arcpy

# Local variables
input_table = r'c:\workspace\LOBtraffic.dbf'
output_fc = r'c:\workspace\SOPA.gdb\lob_traf001'

# BearingDistanceToLine
arcpy.BearingDistanceToLine_management(input_table, output_fc, 'X', 'Y', 
                                       'NAUTICAL_MILES', 'azim', 'DEGREES', 
                                       'GEODESIC', 'recnum')