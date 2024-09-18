# Name: SetClusterTolerance_Example.py
# Description: Updates the cluster tolerance property on a topology

# Import system modules
import arcpy

arcpy.SetClusterTolerance_management("D:/Calgary/Trans.mdb/Streets/Street_Topo", 0.00015)