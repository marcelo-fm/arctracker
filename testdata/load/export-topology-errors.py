# Set the necessary product code
import arceditor

# Import arcpy module
import arcpy

# Local variables:
co_topo_FD_Topology = "C:/Testing/topology.gdb/my_topo_FD/my_topo_FD_Topology"

# Process: Export Topology Errors
arcpy.management.ExportTopologyErrors(co_topo_FD_Topology, 
                                      "C:/Testing/topology.gdb/my_topo_FD", 
                                      "my_topo_FD_Topology")