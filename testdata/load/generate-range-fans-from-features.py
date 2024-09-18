# Description: Select sensors with a distance-based blind spot (a minimum distance greater than zero) and generate fans.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:\Data.gdb"
arcpy.env.overwriteOutput = True

# Select points from sensor layer
sensors = "RangeFanInputFeatures"
outputSensors = "Partial_View"
whereClause = "min_range > 0"
arcpy.Select_analysis(sensors, outputSensors, whereClause)

# Generate range fans from sensors
outputFans = "Fans"
arcpy.GenerateRangeFansFromFeatures_defense(outputSensors, outputFans,
                                            "min_range", "max_range",
                                            "left_az", "right_az")