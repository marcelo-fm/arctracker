# Description: Adds a rule to a topology

# Import system modules
import arcpy

# Any intersection of ParcelOutline (BlockLines subtype only) needs to be reviewed
arcpy.management.AddRuleToTopology("C:/data/Landbase.gdb/LegalFabric/topology", 
                                   "Must Not Intersect (Line)",
                                   "C:/data/Landbase.gdb/LegalFabric/ParcelOutline",
                                   "BlockLines")