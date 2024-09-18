# Find intersections, assign a unique value, and create a buffer.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/data.gdb"

# Find intersections
input_lines = "Streets"
output_intersections = "intersection_subset"
arcpy.defense.LetterIntersections(input_lines,
                                  output_intersections,
                                  "intersection_id",
                                  "aoi",
                                  "UL",
                                  "A_B_C",
                                  "A",
                                  "L;O",
                                  None,
                                  "ADD_DISTANCE")

# Create buffers
arcpy.analysis.Buffer(output_intersections,
                      "intersection_buffers",
                      "40 Feet")