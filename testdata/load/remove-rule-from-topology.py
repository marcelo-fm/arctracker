# Name: RemoveRuleFromTopology_Example.py
# Description: Removes a rule from a topology

# Import system modules
import arcpy

topo = "C:/CityData.mdb/LegalFabric/topology"
rule = "Must Not Have Dangles (21)"
arcpy.RemoveRuleFromTopology_management(topo, rule)