# Description: Deletes a branch version

# Import system modules
import arcpy

# Set local variables
inWorkspace = "https://myserver.mydomain.com/server/rest/services/MyService/FeatureServer"
versionName = "PORTALUSER1.newversion2"

# Run DeleteVersion
arcpy.management.DeleteVersion(inWorkspace, versionName)