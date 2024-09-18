# Description: Generate range rings around active airports

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Select points from airports from input
airports = "Airports"
active = "Active_Airports"
whereClause = "Active = 'Yes'"
arcpy.Select_analysis(airports, active, whereClause)

# Generate Range Rings around selected airports
outputRings = "Rings"
outputRadials = "Radials"
ringType = "MIN_MAX"
distType = "KILOMETERS"
arcpy.GenerateRangeRings_defense(active,
                                 outputRings,
                                 ringType,
                                 outputRadials,
                                 4,
                                 distType,
                                 5, 100, 200, 4000)