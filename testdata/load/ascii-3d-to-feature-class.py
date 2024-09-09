'''****************************************************************************
Name: ASCII3D_to_Feature_Class Example
Description: Creates a TIN surface using XYZI files in a folder and breaklines
             imported from ASCII files.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Define the spatial reference using the name
sr = arcpy.SpatialReference("Hawaii Albers Equal Area Conic")

# Create the elevation points
arcpy.ddd.ASCII3DToFeatureClass("Elevation Points", "XYZI",
                               "elevation_points.shp",
                               "MULTIPOINT", z_factor=3.28,
                               input_coordinate_system=sr,
                               average_point_spacing=2.5,
                               file_suffix="XYZ")

# Create the break lines
arcpy.ddd.ASCII3DToFeatureClass("brklines.gen", "GENERATE",
                               "breaklines.shp",
                               "POLYLINE", z_factor=3.28,
                               input_coordinate_system=sr)

arcpy.ddd.CreateTin("elevation_tin", sr,
                    [["breaklines.shp", "Shape", "hardline"],
                    ["elevation_points.shp", "Shape", "masspoints"]],
                    "CONSTRAINED_DELAUNAY")