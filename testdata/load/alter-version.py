# Description: Changes the description of a version

# Import system modules
import arcpy

# Set local variables
inWorkspace = "https://myserver.mydomain.com/server/rest/services/MyService/FeatureServer"
versionName = "portaluser1.myVersion"
newDesc = "Ready for reconcile and post"

# Sign in to ArcGIS Enterprise
arcpy.SignInToPortal("https://myserver.mydomain.com/portal", 'portaluser1', 'my.password')

# Run AlterVersion
arcpy.management.AlterVersion(inWorkspace, versionName, "", newDesc, "")