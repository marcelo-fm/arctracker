# Name: AddFeatureClassToTopology_Example.py
# Description: Adds a feature class to participate in a topology

# Import system modules
import arcpy

arcpy.management.AddFeatureClassToTopology("D:/Calgary/Trans.gdb/Streets/Street_Topo", "D:/Calgary/Trans.gdb/Streets/StreetNetwork", 1, 1)