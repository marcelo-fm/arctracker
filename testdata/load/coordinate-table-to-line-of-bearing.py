# Description: Create lines of bearing from tabular data and then create 
#              bounding envelopes around each line.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Create lines of bearing
input_table = r"C:/CSV/TableToLineOfBearing.csv"
result_line = "Output_LOB"
arcpy.CoordinateTableToLineOfBearing_defense(input_table,
                                             result_line,
                                             "x",
                                             "Orientation",
                                             "Distance",
                                             "DD_2",
                                             "DEGREES",
                                             "KILOMETERS",
                                             "y")

# Create envelopes
result_envelope = "Output_Envelope"
arcpy.FeatureEnvelopeToPolygon_management(result_line, result_envelope)