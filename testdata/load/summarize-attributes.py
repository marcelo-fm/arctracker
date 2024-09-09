# Name: Summarize Attributes.py
# Description: Summarize Crime Data by year and beat.

# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/CityData.gdb"

# Set local variables
inFeatures = "ChicagoCrimes"
summaryFields = ["Year", "Beat"]
summaryStatistics = [["Arrest", "COUNT"], ["District", "COUNT"]]
out = 'SummarizeCrimes'

# Run SummarizeAttributes
arcpy.gapro.SummarizeAttributes(inFeatures, out, summaryFields, 
                                summaryStatistics)