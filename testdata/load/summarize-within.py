# Name: SummarizeWithin.py
# Description: Summarize river polylines by counties.

# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/RedRiver_basin.gdb"

# Set local variables
summarizedLayer = "Rivers"
summaryPolys = "Basins"
summaryStatistics = [["Width", "MEAN", "RATE"]]
weightedSummaryStatistics = [["DOC", "STDDEV", "COUNT"]]
out = 'SummarizedRivers'


# Run SummarizeWithin
arcpy.gapro.SummarizeWithin(summarizedLayer, out, "POLYGON", None, 
                            None, summaryPolys, "ADD_SUMMARY", 
                            "KILOMETERS", summaryStatistics, 
                            weightedSummaryStatistics)