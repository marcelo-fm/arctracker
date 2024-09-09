# Name: ChangeVersionBranchVersioning.py
# Description: Use the ChangeVersion tool to change the branch version of a feature service
#              layer that has the version management capability enabled.

# Import system modules 
import arcpy

# Sign into ArcGIS Enterprise
arcpy.SignInToPortal("https://myserver.mydomain.com/portal", 'portaladmin', 'my.password')

# Create a variable for the feature service URL
myFS = "https://myserver.mydomain.com/server/rest/services/BranchVersioningData/FeatureServer/0"

# Create the layers
arcpy.management.MakeFeatureLayer(myFS, 'myFSLayer')

# Change to a branch version named myVersion
arcpy.management.ChangeVersion('myFSLayer', "BRANCH", "portaladmin.myVersion")