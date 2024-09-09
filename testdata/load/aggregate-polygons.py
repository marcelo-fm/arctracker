# Name: AggregatePolygons_Example2.py
# Description: Aggregate grass features and then transfer attributes
 
# Import system modules
import arcpy
  
# Set environment settings
arcpy.env.workspace = "C:/data/Portland.gdb/Vegetation"
 
# Set local variables
inGrassFeatures = "grass"
aggregatedFeatures = "C:/data/PortlandOutput.gdb/grassland"
aggregatedTable = "C:/data/PortlandOutput.gdb/grassland_Tbl"
frequencyTable = "C:/data/PortlandOutput.gdb/frequency_Tbl"

# Aggregate grass polygons.
arcpy.cartography.AggregatePolygons(inGrassFeatures, aggregatedFeatures, 50, 
                                    300, 300, "NON_ORTHOGONAL", "", 
                                    aggregatedTable)

# Join the aggregatedTable with input and transfer the COUNT field to 
# aggregatedTable.
arcpy.management.JoinField(aggregatedTable, "INPUT_FID", inGrassFeatures, 
                           "OBJECTID", "COUNT")
 
# Use Frequency on aggregatedTable and obtain sum for COUNT.
arcpy.analysis.Frequency(aggregatedTable, frequencyTable, "OUTPUT_FID", "COUNT")

# Join the aggregatedFeatures with frequencyTable and transfer the COUNT 
# field to aggregatedFeatures.
arcpy.management.JoinField(aggregatedFeatures, "OBJECTID", frequencyTable, 
                           "OUTPUT_FID", "COUNT")