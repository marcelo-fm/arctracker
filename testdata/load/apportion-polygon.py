# Name: Store Service Area Get Population.py
# Description: Use apportionment to transfer population figures to different 
#              geometry.

# Import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/MyAnalysis.gdb"

# Perform apportionment
inputDataWithPop = "CensusBlockGroups"
popField = "Pop2020"
targetServiceAreas = "Store_ServiceAreas"
outputApp = "Store_ServiceAreas_w_Population"
apportionMethod = "AREA"
keepTargetGeom = "MAINTAIN_GEOMETRIES"
arcpy.analysis.ApportionPolygon(inputDataWithPop, popField, targetServiceAreas, 
                                outputApp, apportionMethod, "", "", 
                                keepTargetGeom)

# Summarize store service area populations by store admin region
outStats = "PopulationPerSalesRegion_tlb"
statsFields = [["Pop2020", "SUM"]]
regionField = "SalesRegion" # Values like North, North-East, etc.
arcpy.analysis.Statistics(outputApp, outStats, statsFields, regionField)