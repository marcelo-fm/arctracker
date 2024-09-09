# Name: Compact_Example.py
# Description: compact a file geodatabase

# Import the system modules
import arcpy

# Set local variables
gdbWorkspace = "C:/data/data.gdb"

arcpy.management.Compact(gdbWorkspace)