# Name: RemoveClassFromTopology_Example.py
# Description: Removes a feature class from participating in a topology

# Import system modules
import arcpy

topo = "C:/Datasets/TestGPTopology.gdb/LegalFabric/topology"
fc = "Parcel_line"
arcpy.RemoveFeatureClassFromTopology_management(topo, fc)