# Description: Creates a new version

# Import system modules
import arcpy

# Set local variables
inWorkspace = "c:/Connections/whistler@gdb.sde"
parentVersion = "dbo.DEFAULT"
versionName = "myVersion"
versionAccess = "PUBLIC"
versionDescription = "Version's description"

# Run CreateVersion
arcpy.management.CreateVersion(inWorkspace, parentVersion, versionName, versionAccess, versionDescription)