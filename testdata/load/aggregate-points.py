# Name: AggregatePoints.py
# Description: Aggregate 311 events into 1 KM Bins.

# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/CityData.gdb"

# Set local variables
inFeatures = "SF311"
summaryFields = ["Year", "Beat"]
summaryStatistics = [["Arrest", "COUNT"], ["District", "COUNT"]]
out = "AggregateWildfires"

# Run Aggregate Points
arcpy.gapro.AggregatePoints(inFeatures, out, "BIN", None, "HEXAGON", 
                            "1 Kilometers")