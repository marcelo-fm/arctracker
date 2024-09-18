# Description: Generate range rings around active airports

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:\Data.gdb"
arcpy.env.overwriteOutput = True

# Select points from airports from input
airports = "Airports"
active = "Active_Airports"
whereClause = "Active = 'Yes'"
arcpy.Select_analysis(airports, active, whereClause)

# Generate Range Fans from selected airports
outputFans = "Range_Fans"
distType = "KILOMETERS"
angleUnits = "DEGREES"
arcpy.GenerateRangeFans_defense(active,
                                outputFans,
                                10,
                                100,
                                90,
                                180,
                                distType,
                                angleUnits)