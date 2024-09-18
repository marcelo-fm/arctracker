# Description: Generate buffers around polygon features created from tabular 
#              data.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Create polygons
input_table = r"C:/DataFolder/TableToPolygon.csv"
result_polygon = "Table2Poly"
arcpy.CoordinateTableToPolygon_defense(input_table,
                                       result_polygon,
                                       "POINT_X",
                                       "DD_2",
                                       "POINT_Y",
                                       "Name",
                                       "VSort")

# Generate buffers around polygons
buffer_result = "Buffered_Polygons"
arcpy.Buffer_analysis(result_polygon, buffer_result, "100 Kilometers")