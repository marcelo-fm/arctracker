# Name: ErasePoint_Example2.py
# Description: Replacing low resolution elevation points inside
# lake areas by high resolution lidar points.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/Portland.gdb/relief"

# Set local variables
inElevationFeatures = "elevation_points"
inLidarFeatures = "lidar_points"
inLakeFeatures = "lakes"

# Erase elevation points inside lakes
arcpy.edit.ErasePoint(inElevationFeatures, inLakeFeatures, "INSIDE")

# Clip lidar points inside lakes
arcpy.edit.ErasePoint(inLidarFeatures, inLakeFeatures, "OUTSIDE")

# Append the clipped lidar points to the remaining elevation points
arcpy.management.Append(inElevationFeatures, inLidarFeatures, "NO_TEST")
