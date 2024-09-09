# Name: GrantPrivileges_Example.py
# Description: Grants view and edit privileges to WendelClark

# Import system modules
import arcpy

# Set local variables
datasetName = "c:/Connections/gdb@production.sde/production.GDB.ctgFuseFeature"

# Run ChangePrivileges
arcpy.management.ChangePrivileges(datasetName, "WENDELCLARK", "GRANT", "GRANT")