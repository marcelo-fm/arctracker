# Name: FeaturesToGPX.py
# Description: Converts line features to a GPX track.

# Import system models
import arcpy

# Convert the line feature file to a GPX track with optional Name Field,
# Description Field, and Date Field
arcpy.conversion.FeaturesToGPX(r'C:\Data\Bike_Routes.gdb\Limekiln_Canyon', r'C:\Data\Output\Limekiln_Canyon.gpx', "RouteName", "SegmentLength", None, "Date")