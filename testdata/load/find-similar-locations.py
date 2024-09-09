#-------------------------------------------------------------------------------
# Name: FindSimilarLocations.py
# Description: Find Similar stores to a top performing store

# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/SalesData.gdb"

# Set local variables
referenceStore = "TopPerformer"
candidateStores = "AllStores"
analysisFields = [ "SickDays", "TotalCustomers", "AvgPurchaseAmount"]
outputName = "BestStores_10"

# Run Find Similar Locations
arcpy.gapro.FindSimilarLocations(referenceStore, candidateStores, 
                                 outputName, analysisFields, 
                                 "MOST_SIMILAR", "ATTRIBUTE_VALUES", 10)